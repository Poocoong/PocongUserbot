#  (C) @pocongonlen
# ⚠️ Do not remove credits.


from userbot.events import poci_cmd
from random import choice, getrandbits, randint

KATAPOCONG = [
    "pawang? apakah itu semacam pimpinan para hewan?",
    "hidup mu saja masih berantakan, makah sok ngurusin hidup orng!",
    "bukan hidup yg sulit , tapi dirimu yg mempersulit",
    "Ulang tahun? kau hanya merayakan kematian mu semakin dekat!",
    "Jangan tanya kenapa aku berubah, liat ultramen dia berubah karena ada masalah.",
    "Percaya diri memang penting, tapi sadar diri lebih penting.",
    "**Mau di hargai , tapi tidak bisa menghargai**.",
    "healing? apakah itu kata agar orang orang peduli dengan mu?",
    "Dia sehat, tetapi tidak sholat!",
    "Baperan? apakah itu kata untuk berlindung setelah menghina?",
    "Pacaran? apa maksudmu berteman dengan cara aneh?",
    "Aku sudah terbiasa melakukannya sendiri! kau cukup diam dan memperhatikannya",
    "Tidak ada sahabat sejati, kecuali kita sendiri.",
    "diam seperti wibu bergerak mencintai mu",
    "Jangan menilai orang dari luar, Aqua saja bisa berisi arak!",
    "Seekor singa tak pernah mengatakan dirinya raja!",
    "Yang tinggi saja tidak melangit, ini tanah sok jadi langit!",
    "Halu adalah kebiasaan orang jelek!",
    "Apakah cinta membuat mu bahagia?",
]


@bot.on(poci_cmd(outgoing=True, pattern=r"quote$"))
async def _(sange):
    """Greet everyone!"""
    await sange.edit(choice(KATAPOCONG))
