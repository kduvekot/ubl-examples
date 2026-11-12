"""Generate the invented vocabularies of Urvanian (qau) and Lisavan (qal) for the words the examples need.

Deterministic: a word's form comes from a hash of the English word, so it never changes once made. Forms that
collide with common words of real languages (Italian, Polynesian, and others in BLOCK) or with words already in
the vocabulary are skipped. The vocabularies live in world/countries.json (languages.qau/qal.lexicon).

When the build reports "words missing from the vocabularies of the world's languages", save that JSON list as
missing.json and run, from the repository root:

    python3 tools/lexicon.py missing.json qau      (Urvanian; or qal for Lisavan, or both when none is given)

then rebuild. Never add words by hand."""
import hashlib, json, re, sys
sys.path.insert(0, "tools")
BLOCK = set("""
la le lo li il un una uno di da de del per con su non che chi ma se si no ne mi ti ci vi io tu lui lei noi voi
casa cosa vita mare sole luna terra porta porto via vino pane mano nero rosso bello buono male bene tutto molto poco
sono sei era ora poi qui qua fra tra sopra sotto dove come mai sempre anche
ali aloha mana tapu moana motu ika fale vai wai tama tane wahine kai kia ora ahi aina lani nui iti manu fanua whenua atua
tangata lua tolu lima ono fitu valu iva sefulu tahi rua toru wha rima whitu waru iwa tekau pule malo lelei fono matai
talofa fakafetai mahalo tapa ava kava taro ulu niu popo api fia mea tea lea nau koe ahau taua matou kaua mai atu ake iho
pea foki kei hei kua ana ona tana tona hoa pai kino roa poto hou matua moa pua ula mele hula lei keiki kane koa nalu
honu mauna pali one papa pono malama kapu kuna lolo pupu poi tiki tapa hapu iwi marae haka kiwi paua pipi titi kumara
tohu tika mate kaka tofu tofa vao salu fete fato nope kali laka mati kana fita lita mika tike nua vone moma tulo tuo tua moo pee boar sao vue voe vio fae tae nae goar papaya banana kokonati faleoloa motuvaka aloalo mamae aroha hui kaupapa mahi moko tino toa tupu utu wairua waka whanau
""".split())
def h(word, lang, salt):
    return int(hashlib.sha256(f"{lang}:{word}:{salt}".encode()).hexdigest(), 16)
def make(word, lang, taken):
    salt = 0
    while True:
        n = h(word, lang, salt); salt += 1
        if lang == "qau":
            ons = ["k", "t", "d", "z", "r", "m", "n", "v", "b", "g", "h", "s", "sk", "dr", "tr", "kr", "zh", "st"]
            vow = "aeiua"; cod = ["", "", "r", "n", "k", "z", "l"]
            k = 1 + (len(word) >= 5) + (salt > 40)
            w = ""
            for s_ in range(k):
                w += ons[n % len(ons)]; n //= len(ons); w += vow[n % 5]; n //= 5
                if s_ < k - 1: w += cod[n % len(cod)]; n //= len(cod)
            w = w[:-1] + ["ek", "an", "ir", "ek", "an", "ir", "ul", "az"][n % 8]   # the ending replaces the last vowel
        else:
            ons = ["", "h", "k", "l", "m", "n", "p", "s", "t", "v", "f", "l", "t", "k"]
            vow = "aeiouaeia"
            k = 3 + (len(word) >= 9)
            w = ""
            for s in range(k):
                o = ons[n % len(ons)]; n //= len(ons)
                if s == 0 and o == "": o = "v"
                w += o + vow[n % len(vow)]; n //= len(vow)
        if w not in BLOCK and w not in taken.values() and not re.search(r"(.)\1\1", w):
            return w
if __name__ == "__main__":
    words = json.load(open(sys.argv[1]))
    c = json.load(open("world/countries.json"))
    langs = c.setdefault("languages", {})
    for code in sys.argv[2:] or ("qau", "qal"):
        lex = langs[code].setdefault("lexicon", {})
        for wd in sorted(words):
            if wd not in lex:
                lex[wd] = make(wd, code, lex)
    open("world/countries.json", "w").write(json.dumps(c, indent=1, ensure_ascii=False) + "\n")
    print("words:", len(langs["qau"]["lexicon"]))
