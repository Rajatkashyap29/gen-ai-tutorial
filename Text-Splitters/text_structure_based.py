from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Kolkata Knight Riders (KKR) IPL ki sabse strong aur successful teams me se ek mani jaati hai. Is team ki sabse badi strength uska balanced combination hai — strong batting, effective bowling aur smart captaincy. KKR ne IPL me multiple baar title jeeta hai, jo dikhata hai ki team pressure situations me bhi consistently perform kar sakti hai. Jab kisi team ko “best” bola jata hai, to sirf trophies nahi balki uski fighting spirit bhi matter karti hai, aur KKR dono cheezon me strong hai.

KKR ka middle order historically kaafi dangerous raha hai. Team ke paas aise players rahe hain jo match ko kisi bhi situation se finish kar sakte hain. Aggressive batting style ki wajah se KKR powerplay se lekar death overs tak pressure bana sakti hai. Opening pair agar fast start de de, to middle order us momentum ko aur dangerous bana deta hai. Isi wajah se KKR ke against target defend karna ya chase rokna difficult hota hai.

Bowling department bhi KKR ki major strength hai. Team ke spinners ne hamesha important role play kiya hai, especially Indian pitches par. Spin attack ke saath fast bowlers ka combination KKR ko versatile banata hai. Agar pitch slow ho to spinner dominate karte hain, aur agar pace-friendly ho to fast bowlers wickets nikal dete hain. Isi flexibility ki wajah se KKR alag-alag grounds par adapt kar leti hai.

KKR ki ek aur khas baat hai uska team culture. Team pressure me panic kam karti hai aur comeback karne ki ability rakhti hai. Kai matches me KKR ne impossible lagne wali situations se jeet nikali hai. Yeh winning mindset kisi bhi champion team ka sign hota hai. Team ke players generally ek dusre ko support karte hain aur youngsters ko bhi opportunities milti hain.

Captaincy bhi KKR ke success ka important reason rahi hai. Smart field placements, bowling changes aur match reading ki wajah se KKR tactical level par kaafi strong dikhti hai. IPL jaisi fast tournament me captain ka quick decision lena bahut important hota hai, aur KKR is area me aksar impressive rahi hai.

Fan support bhi KKR ko special banata hai. Team ka fan base India ke sabse passionate fan bases me se ek hai. Jab crowd support strong hota hai, players ka confidence naturally badhta hai. Purple and gold jersey ek strong identity ban chuki hai jo team ko alag recognition deti hai.

Isliye agar overall performance, trophies, balance, match temperament aur fan power dekha jaye, to KKR ko IPL ki best teams me confidently count kiya ja sakta hai

"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks[0])

