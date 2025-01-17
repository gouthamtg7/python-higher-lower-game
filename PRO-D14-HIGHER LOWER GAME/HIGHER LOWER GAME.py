import random
print('''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/        
''')
#BUILD A DICTIONARY
dic = {
    "Cristiano Ronaldo, footballer, from Portugal, 5-time Ballon d'Or winner": 600000000,
    "Lionel Messi, footballer, from Argentina, 7-time Ballon d'Or winner": 480000000,
    "Dwayne Johnson, actor, from USA, known as 'The Rock'": 370000000,
    "Kylie Jenner, entrepreneur, from USA, founder of Kylie Cosmetics": 400000000,
    "Ariana Grande, singer, from USA, known for her four-octave vocal range": 370000000,
    "Selena Gomez, singer, from USA, former Disney star turned pop icon": 380000000,
    "Kim Kardashian, TV personality, from USA, star of 'Keeping Up with the Kardashians'": 370000000,
    "Beyoncé, singer, from USA, former lead singer of Destiny's Child": 320000000,
    "Justin Bieber, singer, from Canada, discovered on YouTube at age 13": 290000000,
    "Taylor Swift, singer, from USA, known for her storytelling through music": 280000000,
    "Kendall Jenner, model, from USA, member of the Kardashian-Jenner family": 250000000,
    "Khloé Kardashian, TV personality, from USA, co-founder of Good American": 290000000,
    "Jennifer Lopez, singer and actress, from USA, known as 'J.Lo'": 250000000,
    "Nicki Minaj, rapper, from Trinidad and Tobago, known for her unique style": 210000000,
    "Miley Cyrus, singer and actress, from USA, former Disney star": 200000000,
    "Kourtney Kardashian, TV personality, from USA, oldest Kardashian sister": 210000000,
    "Kevin Hart, comedian and actor, from USA, known for his stand-up comedy": 160000000,
    "Virat Kohli, cricketer, from India, former captain of the Indian national team": 250000000,
    "Katy Perry, singer, from USA, known for hits like 'Roar' and 'Firework'": 160000000,
    "Shakira, singer, from Colombia, known for her hit 'Hips Don't Lie'": 160000000,
    "Cardi B, rapper, from USA, known for her candid social media presence": 170000000,
    "LeBron James, basketball player, from USA, plays for the LA Lakers": 160000000,
    "Chris Hemsworth, actor, from Australia, known for playing Thor": 160000000,
    "Rihanna, singer and entrepreneur, from Barbados, founder of Fenty Beauty": 240000000,
    "Ellen DeGeneres, TV host, from USA, host of 'The Ellen DeGeneres Show'": 120000000,
    "David Beckham, footballer, from England, co-owner of Inter Miami CF": 80000000,
    "Zendaya, actress and singer, from USA, star of 'Euphoria'": 190000000,
    "Shawn Mendes, singer, from Canada, known for his hit 'Stitches'": 72000000,
    "Billie Eilish, singer, from USA, known for her unique style and sound": 110000000,
    "Will Smith, actor, from USA, known for 'The Fresh Prince of Bel-Air'": 74000000,
    "Tom Holland, actor, from England, known for playing Spider-Man": 66000000,
    "Priyanka Chopra, actress, from India, winner of Miss World 2000": 90000000,
    "Robert Downey Jr., actor, from USA, known for playing Iron Man": 54000000,
    "Gal Gadot, actress, from Israel, known for playing Wonder Woman": 73000000,
    "Vin Diesel, actor, from USA, known for the 'Fast & Furious' series": 83000000,
    "Chris Evans, actor, from USA, known for playing Captain America": 72000000,
    "Hrithik Roshan, actor, from India, known for his dancing skills": 46000000,
    "Emma Watson, actress, from England, known for playing Hermione Granger": 70000000,
    "Johnny Depp, actor, from USA, known for 'Pirates of the Caribbean'": 12000000,
    "Mark Wahlberg, actor, from USA, known for 'Transformers' and 'Ted'": 19000000,
    "Scarlett Johansson, actress, from USA, known for playing Black Widow": 57000000,
    "Zac Efron, actor, from USA, known for 'High School Musical'": 57000000,
    "Snoop Dogg, rapper, from USA, known for his West Coast rap style": 82000000,
    "Jennifer Aniston, actress, from USA, known for 'Friends'": 42000000,
    "Bruno Mars, singer, from USA, known for 'Uptown Funk'": 27000000,
    "Drake, rapper, from Canada, known for hits like 'Hotline Bling'": 140000000,
    "Lady Gaga, singer, from USA, known for her hit 'Bad Romance'": 52000000,
    "Adele, singer, from England, known for her powerful voice": 54000000,
    "Ed Sheeran, singer, from England, known for his hit 'Shape of You'": 42000000,
    "Dua Lipa, singer, from England, known for her album 'Future Nostalgia'": 83000000,
    "Post Malone, rapper, from USA, known for his hit 'Circles'": 27000000,
    "Camila Cabello, singer, from USA, known for 'Havana'": 65000000,
    "Travis Scott, rapper, from USA, known for 'Astroworld'": 48000000,
    "Jason Momoa, actor, from USA, known for playing Aquaman": 17000000,
    "Millie Bobby Brown, actress, from England, star of 'Stranger Things'": 65000000,
    "Shah Rukh Khan, actor, from India, known as the 'King of Bollywood'": 32000000,
    "Gigi Hadid, model, from USA, known for her work with Victoria's Secret": 76000000,
    "Bella Hadid, model, from USA, sister of Gigi Hadid": 58000000,
    "Anushka Sharma, actress, from India, wife of Virat Kohli": 62000000,
    "Deepika Padukone, actress, from India, known for 'Padmaavat'": 72000000,
    "Ranveer Singh, actor, from India, known for his energetic performances": 43000000,
    "V, singer, from South Korea, member of BTS": 70000000,
    "Jungkook, singer, from South Korea, member of BTS": 90000000,
    "Suga, rapper, from South Korea, member of BTS": 50000000,
    "RM, rapper, from South Korea, leader of BTS": 50000000,
    "J-Hope, rapper, from South Korea, member of BTS": 49000000,
    "Jin, singer, from South Korea, member of BTS": 45000000,
    "Jimin, singer, from South Korea, member of BTS": 51000000,
    "BLACKPINK Lisa, singer, from Thailand, member of BLACKPINK": 96000000,
    "BLACKPINK Jennie, singer, from South Korea, member of BLACKPINK": 78000000,
    "BLACKPINK Rosé, singer, from New Zealand, member of BLACKPINK": 69000000,
    "BLACKPINK Jisoo, singer, from South Korea, member of BLACKPINK": 64000000,
    "IU, singer, from South Korea, known for her hit 'Good Day'": 28000000,
    "Lee Min Ho, actor, from South Korea, known for 'Boys Over Flowers'": 31000000,
    "Park Seo Joon, actor, from South Korea, known for 'Itaewon Class'": 22000000,
    "Gong Yoo, actor, from South Korea, known for 'Goblin'": 23000000,
    "Kim Soo Hyun, actor, from South Korea, known for 'My Love from the Star'": 27000000,
    "Kylian Mbappe, footballer, from France, plays for Paris Saint-Germain": 100000000,
    "Paul Pogba, footballer, from France, known for his midfield prowess": 54000000,
    "Antoine Griezmann, footballer, from France, plays for Atletico Madrid": 35000000,
    "Sergio Ramos, footballer, from Spain, plays for Paris Saint-Germain": 53000000,
    "Gerard Pique, footballer, from Spain, former Barcelona star": 20000000
}
#Define and declare non iterable stuff for while loop
win = str()
score = 0
dic_keys = list(dic.keys())
dic_followers = list(dic.values())
selected_A = dict()
selected_B = dict()
A = list(selected_A.keys()) #Selected A keys
B = list(selected_A.values()) #Selected A followers
C = list(selected_B.keys())#Selected B keys
D = list(selected_B.values())#Selected B followers
game_over = False
x= int()
y= int()
#PICK RANDOM KEYS AND VALUES FROM THE DICTIONARY AND STORE THEM
def select_A(score):
    """To Select the comparison keys of A set.It is selected newly only once."""
    global x
    if score == 0:
         x = random.choice(dic_keys)
         selected_A [x] = dic[x]
    else :
        x = C[-1]  # Assign last B to A
        selected_A[x] = dic[x]
def select_B(score):
    """To Select the comparison keys of B set. It is new everything time"""
    global y
    y = random.choice(dic_keys)
    selected_B[y] = dic[y]
def ensure_not_same():
    while x == y:
        select_B(score)
    A.append(x)
    B.append(dic[x])
    C.append(y)
    D.append(dic[y])


#Start the loop
while (game_over==False):
    select_A(score)
    select_B(score)
    ensure_not_same()

    s1 = input(f'''Compare\nA:{A[-1]}\n 
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
\nB:{C[-1]}\nWho has more instagram followers??(A/B)\n''')
    if B[-1]>D[-1]:
        win = "A"
    elif B[-1]<D[-1]:
        win = "B"
    else :
        score +=1
    if s1==win:
        score+=1
        print(f"Current Score : {score}")
    elif s1!=win:
        print(f"Your Final Score : {score}")
        game_over = True
    else :
        print(("Invalid input"))






