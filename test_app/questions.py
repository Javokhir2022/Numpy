# -*- coding: utf-8 -*-
"""questions.txt faylini o'qib, savollar ro'yxatiga aylantiradi.

Kutilayotgan format:

    1. Python qaysi tilda yozilgan?
    A) C #
    B) Java
    C) Pascal
    D) Assembler

    2. ...

Qoidalar:
  * Savol raqam bilan boshlanadi: "1." yoki "1)" yoki "1 -"
  * Keyingi qatorlar -- variantlar. Harf prefiksi (A) a. 1)) ixtiyoriy.
  * To'g'ri javob qatorida "#" belgisi turadi (boshida yoki oxirida farqi yo'q).
  * Bir nechta variantda "#" bo'lsa -- ko'p javobli savol bo'ladi.
  * "//" yoki ";" bilan boshlangan qator -- izoh, e'tiborga olinmaydi.
"""

import re

SAVOL_BOSHI = re.compile(r"^\s*(\d+)\s*[\.\)\-:]\s*(.*)$")
VARIANT_PREFIKS = re.compile(r"^\s*([A-Za-zА-Яа-яЎўҚқҒғҲҳ])\s*[\.\)]\s+(.*)$")


class ParseXato(Exception):
    pass


def _tozala(qator):
    """Qatordan '#' belgisini olib tashlaydi va to'g'ri javobligini qaytaradi."""
    togri = "#" in qator
    matn = qator.replace("#", "").strip()
    return matn, togri


def parse_matn(matn):
    savollar = []
    joriy = None
    xatolar = []

    for raqam, xom in enumerate(matn.splitlines(), start=1):
        qator = xom.strip()
        if not qator or qator.startswith("//") or qator.startswith(";"):
            continue

        bosh = SAVOL_BOSHI.match(qator)
        # Raqamli qator faqat yangi savol bo'la oladi -- variantda '#' bo'lishi
        # yoki oldingi savolda variant bo'lishi mumkin emas degani emas, shuning
        # uchun '#' bo'lgan raqamli qatorni variant deb hisoblaymiz.
        if bosh and "#" not in qator:
            if joriy is not None:
                savollar.append(joriy)
            savol_matni, _ = _tozala(bosh.group(2))
            joriy = {
                "raqam": int(bosh.group(1)),
                "qator": raqam,
                "matn": savol_matni,
                "variantlar": [],
                "togri": [],
            }
            continue

        if joriy is None:
            xatolar.append("{}-qator: savoldan oldin matn bor -> {!r}".format(raqam, qator))
            continue

        # Savol matni bo'sh bo'lsa, bu qator savolning davomi
        if not joriy["matn"]:
            joriy["matn"], _ = _tozala(qator)
            continue

        pref = VARIANT_PREFIKS.match(qator)
        xom_variant = pref.group(2) if pref else qator
        variant, togri = _tozala(xom_variant)
        if not variant:
            continue
        joriy["variantlar"].append(variant)
        if togri:
            joriy["togri"].append(len(joriy["variantlar"]) - 1)

    if joriy is not None:
        savollar.append(joriy)

    # Tekshiruv
    for s in savollar:
        if len(s["variantlar"]) < 2:
            xatolar.append(
                "{}-savol ({}-qator): variant soni 2 tadan kam".format(s["raqam"], s["qator"])
            )
        if not s["togri"]:
            xatolar.append(
                "{}-savol ({}-qator): to'g'ri javob '#' bilan belgilanmagan".format(
                    s["raqam"], s["qator"]
                )
            )

    if not savollar:
        xatolar.append("Birorta ham savol topilmadi.")

    if xatolar:
        raise ParseXato("\n".join(xatolar))

    for i, s in enumerate(savollar):
        s["id"] = i
    return savollar


def yukla(yol):
    with open(yol, encoding="utf-8-sig") as f:
        return parse_matn(f.read())


if __name__ == "__main__":
    import sys

    yol = sys.argv[1] if len(sys.argv) > 1 else "questions.txt"
    try:
        qs = yukla(yol)
    except ParseXato as e:
        print("XATO:\n" + str(e))
        raise SystemExit(1)
    print("Jami {} ta savol o'qildi.\n".format(len(qs)))
    for s in qs:
        print("{}. {}".format(s["raqam"], s["matn"]))
        for i, v in enumerate(s["variantlar"]):
            belgi = " <-- TO'G'RI" if i in s["togri"] else ""
            print("   {}) {}{}".format("ABCDEFGH"[i], v, belgi))
        print()
