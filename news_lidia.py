import streamlit as st

# Configuração da página
st.set_page_config(page_title="Lídia News", layout="centered")

# Título da aplicação
st.title("📜 Lídia News – Week edition")

# Estilo personalizado com CSS
st.markdown(
    """
    <style>
    .custom-container {
        background-image: url('https://www.toptal.com/designers/subtlepatterns/uploads/paper.png'); /* Link para textura de papel */
        background-size: cover;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #d4a373;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif;
        line-height: 1.6;
        color: #4b3621;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Conteúdo da carta com botão
if st.button("Letter - 23 jan💌"):
    st.markdown(
        """
        <div class="custom-container">
            <h3>23/01 – Week Edition</h3>
            <strong>Writer:</strong> <em>Small puff pastry with a flavored cream in the middle</em>
            <p></p>
            <p>This week I tried to get back to my old routine, which was going to bed early to wake up early and go to the gym, but my knee still feels weird, so when I work out, I just feel like I'm doing it all the time kkkkkk.</p>
            <p>I went back to writing my master's thesis. I took a break from looking for a job because it makes me very anxious and a little doubtful of myself, but two companies that I had already sent my CV to scheduled a call for tomorrow.</p>
            <p>Yesterday I had a very healthy dinner with Doritos and wine kkkkk.</p>
            <p>And I don't know how it is for you, but I can't stand January anymore kkkkk.</p>
            <p>Today I was really pissed because Iga, the second best tennis player in the world, lost, and ruined the perfect final that was supposed to be on Saturday.</p>
            <p>I think my PMS is starting yesterday, so I think I'll spend the weekend resting, I just plan on visiting my mother. I'm also trying to get the courage to redo my braids this weekend. I have a lot of hair... if we had a child, he'd be like the Itt from the Addams family hahaha</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Adicionando a imagem
    st.image(
        "https://www.fashionbubbles.com/wp-content/uploads/2021/04/059d3dd130b7e8387eac4e0391e3c8df.jpg",
        caption="Itt, Addams Family",
        use_container_width =True,
    )
    
    # Frase seguinte
    st.markdown(
        """
        <div class="custom-container">
            <p>And you, did you manage to get that girl to stop bothering you? When I went through a similar situation, I didn't even reply, I just archived the message to avoid more problems.</p>
            <p>What about theater studies? Does your church have a theater group?</p>
            <p>How's the weather there? Do you want me to send you about 5°C from here? Haha</p>
            <p>I confess that on Sunday I was saddo knowing that I wouldn't have your attention like I used to. It was a bit selfish of me, I know rsrs, but who told you to be like Jesus? My mother teach me to always talk to Jesus, hahaha. But after a while I thought about it and realized that in less than 4/5 months neither you would come back here, nor would I be able to save up money to visit you, so I was calm again. Besides, it's a good time for us to get to know each other well, create a friendship, and it's good to know that someone is talking to me for more than just my body, not that I have a problem with that, I love my body and I love it when people are attracted to it, I love exchanging hot messages, but I don't like it when people just describe me as a big butt, you know? I've binge-watched all the Marvel movies to get a lot of content, and it's a waste to just describe me as a butt, even if it's big hahaha.</p>
            <p>Ahh, I saw another movie you sent me, Kal ho Na hoo. I know you said that Shah Rukh is a heartthrob in India, but I still think you're more handsome than him (and only my opinion matters lol.. I think I'll just watch one or two more and leave the rest for to watch by your side.</p>
            <p>And I know you must be wondering "why does this crazy girl still talk to me?! And do she still think we'll see each other again?!" hahaha but if you put up with me for another month, I'll tell you, if not you'll never know👀 kkkkkk</p>
            <p>Well, next week I'll be back with more Lídia news hahah</p>
            <p>I hope you had a blessed week, kisses on your breasts and a bite on your ear 😘</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if st.button("Letter +18 - 26 jan💋"):
    st.markdown(
        """
        <div class="custom-container">
            <h3>26/01 – Week Edition</h3>
            <strong>Writer:</strong> <em>Your fucking idiot</em>
            <p></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    colx1, colx2, colx3 = st.columns([1, 2, 1])
    
    with colx2:
        st.image(
            "family.jpg",
            caption="FIRST, our future happy family🙃",
            use_container_width =False, width=300,
        )
            
    st.markdown(
        """
        <div class="custom-container">
            <p>First, I don’t wanna hear ONLY that WAS a beautiful time that we livED and WAS good the energy that we sharED, all in past, okay?! ... because I’m sending my energy and affections for the letters, Did you wont received? If not, I will have to complain to the mail service hahaha</p>
            <p></p>
            <p>We'll meet in person again, okay? ...we'll probably get married too, we'll have kids, who knows?!.. God knows 👀 Kkk </p>
            <p>I'll only give up of see you if you don't want me anymore rsrs. Otherwise, I have plans to come visit you later this year, even if it's on 12/31 hahahah, and if you want to come earlier, you can stay here at my house, I'll even make a copy of the key for you kkkkk. </p>
            <p>Annnd ughhh your breast muscle it been big already, in the next answer vídeo, you can be without tshirt to me to analize better 😉</p>
            <p>Babe, why a Golden retriever needs 2 pre work?? Why??? </p>
            <p>Be careful, okay my love? I know that you wants fast results, but don't lose of your eyes your health too... You have to have health to put up me while I ride on you hahah</p>
            <p>I wasn't going to send a letter today, but you visited my mind all night... and I'm warning you right now, this letter is a little bit +18🙃</p>
            <p></p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
    cola1, cola2, cola3 = st.columns([1, 2, 1])

    with cola2:
        st.video("gif.mp4")
        
    st.markdown(
        """
        <div class="custom-container">        
            <p>Mr. Ryan, you back to your country and left a little you in my mind telling "chickens" all day hahaha (send me this vídeo pleaseee haha) </p>
            <p>I miss your kisses, you pressing me against the wall, holding my neck, looking into my eyes while you caressed me. </p>
            <p>I miss you putting my breasts in your mouth, your kisses on my pussy. Oh, I really regret not letting you cum inside me. I know I would be crazy with fear of getting pregnant hahaha, but now I have to imagine what it would be like to have you inside me, cumming for me and moaning in my ear. You move me, boy, a lot... and do you know what's the worst? Or the best for you? rsrs... that you moved me by just being yourself, doing and saying little things, and with that beautiful way of looking at me. </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image(
            "look.jpeg",
            caption="I'm in love for this photo",
            use_container_width =False, width=300,
        )
    
    st.markdown(
        """
        <div class="custom-container">
            <p>I wish I could be killing the heat of Rio with you in the shower or bathtub, massaging your back with soap, with my breasts too, running my hand all over your body, and whispering something stupid in your ear to see your smile. </p>
            <p>Get ready, love, because the next time I see you, I'll be wearing beautiful lingerie and we'll spend hours locked in a room... Talking, making love, making you laugh, making love in a dog style, laughing at the stupid things you say, and fucking on the table hahaha</p>
            <p>I miss you my boy. Receive my kisses that are full of love and horniness  😘🫦</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if st.button("BIG Letter - 30 jan❤️"):
    st.markdown(
        """
        <div class="custom-container">
            <h3>30/01 – Week Edition</h3>
            <strong>Writer:</strong> <em>A different girl</em>
            <p></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
            
    st.markdown(
        """
        <div class="custom-container">
            <p><p>Ry, first I wanted to know how you are... I'm worried about you... I know you said you would be more off and such, but I don't know, I don't feel like you're doing very well... You're not eating the way you like, you spend the day working or studying, and it's cold there, which doesn't help you stay happy rsrs, and you're still without me, which I imagine must be the hardest part kkkk... So, my love, how are you REALLY doing? </p>
            <p></p>
            <p>I'm praying for you got a good modeling or acting contract here in Rio, and u would have to spend about 2/3 months here hahaha </p>
            <p>Don't worry, my air conditioner should arrive in this week here</p>
            <p></p>
            <p>This week was tiring rsrs... I had the second phase of the interviews I did, I'm tired of telling you about my professional trajectory kkkk. I had to do two huge technical tests, I finished one this morning, at 3 am, and I just finished the last one now, before sending you this letter 😪. I'm dead and very hungry lol. And at work at the beginning of the week it seemed like nothing was going well. </p>
            <p>Aaanddd babe What's happening with the world in this 2 days?! Death in a religion ceremony in India, yesterday was a terrible rain here in Rio, the water in street was upper the bus, our cellphones in the streets received alert from the government... There in US had a unbelievable accident, the helicopter had already seen the plane from a distance, the control tower had already informed them and even so they collided .... Be safa there my boy, I'm praying for u, and pray to me and my family too🙏🏼  (by the way, we are all fine from yesterday's rain🙌🏼)</p>
            <p></p>
            <p>Ahh, I'm teaching English to my niece, look at that (spreading Sims English to the world hahaha) </p>
            <p></p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
    cola1, cola2, cola3 = st.columns([1, 2, 1])

    with cola2:
        st.video("Isa.mp4")
        
    st.markdown(
        """
        <div class="custom-container">        
            <p>Funny thing is that this weekend I was on my period... and when I'm like that I get really clumsy... One time I went to a two-story store, but they put shelves with products on the stairs, can you believe I managed to knock over half of the shelves while I was trying to climb the stairs?! kkkkkk</p>
            <p>All I could do was look at the things on the floor and at the store saleswoman, who was killing me with her eyes kkkk... I tried to offer help, but she was so pissed off and scared, she just wanted me to not touch anything else kkkkkkkk. </p>
            <p>Then this weekend I got really sick with cramps, so I stayed with my mother on Friday and Saturday to be taken care of by her. Then one day I felt like eating fried cassava, so I went to cook it, forgot about it on the stove and the pan dried out. When I was frying it, I managed to make the oil splash and burn my arm... I got kicked in the face by my niece while she was sleeping, I went to walk in the yard, slipped and hurt my little finger, kkkkkk... I'm a walking danger to myself, with PMS... So I went back home and stayed quiet... I only went out on Sunday to make a delivery for my brother and to see a show that was on the beach. </p>
            <p>Sometimes I think life is so unfair... there are a lot of idiots guys after me, there are nice guys too, but it's hard to find someone who seems everything its fine, you know? The people I've met in the last few years are nothing like me, and there's a guy who's crazy like me, with a totally childish sense of humor like mine, who's good with the people around him, sees life in a beautiful way, like I do see it, who's confident in himself, who managed to see behind the big wall I have, a Man who made me sure of what I wanted, but he simply lives in another country, and a country with 300 bureaucracies to get into... Why life couldn't be a little easier sometimes rsrs</p>
            <p>Sometimes I feel like an idiot writing these letters, like Ted Mosby or in the movie The Lake House kkkkkk, and I also don't know if it's serving the purpose I wanted, of bringing us more closer, even in the midst of the crazy routine. But like the good Ted Mosby that I am, I have to believe in my fairy tale kkkk. And it's good to smile again when I see a message notification. My romantic soul hopes that these letters are helping my Sims continue building his house inside your heart kkkkkk. But if they're at least helping to make you smile in this difficult routine of yours, I'll be happy. 💛</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image(
            "ted.jpg",
            caption="Ted Mosby",
            use_container_width =False, width=300,
        )
    
    st.markdown(
        """
        <div class="custom-container">
            <p>How crazy it must have been in the past, people would send letters, wait days for them to arrive, and then more days for the answer to come. </p>
            <p></p>
            <p>Ry, I'm amazed at how I can open up to you. Those who know me know that I'm a very closed person when it comes to what I'm feeling and what I want, and I don't know... I feel good talking about myself with you. I'm even thinking about the next letter being something like "Who is Lídia?" kkkkkk. If you have any questions, leave them in my inbox kkkkkk. </p>
            <p></p>
            <p>I said too much in this letter né?! but it's my hormones' fault, they were agitated this week kkkk🤷🏼‍♀️🙃</p>
            <p></p>
            <p>Ahh, I'll let you choose the day of our next teledate, okay?... I can only do it after 8pm BR on weekdays. </p>
            <p></p>
            <p></p>
            <p>I miss u!</p>
            <p></p>
            <p></p>
            <p>Receive my kisses with much affection😘❤️</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Open your letter talking about Ryan - 09 fev💋"):
    st.markdown(
        """
        <div class="custom-container">
            <h3>09/02 – Week Edition</h3>
            <strong>Writer:</strong> <em>Me</em>
            <p></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="custom-container">
            <p>Hi babe, </p>
            <p>How was the doctor? </p>
            <p>Here this week was the same, more interview, English test, work... I was visit my friends new house, we did a little party rsrs a drunk a lot that I finished slept on the table hahaha </p>
            <p>And today is a birthday of one of my friends, and she choose celebrate in that japanese restaurant, that we ate ... today and that day was nice</p>
            <p>A friend and I tried to install the air-conditioning, but it was terrible hahahahah... it's too big for the space I had to install it, and the screws were very rusty... I'll have to wait for my brother to have time to come here and fix it</p>
            <p></p>
            <p>I never asked before, did you do a college? </p>
            <p></p>
            <p>I realized that a know almost nothing about u ... and how this week I dont have a lot things to say, let talk about u rs</p>
            <p>I know that your family it's from Guiana, I know that you have bad boys around u in your childhood, and also know that you survives from this guy's and now u are modeling while they probably aren't too handsome like u (they are probably bald hahah)... I know that you a man that always figure out a way to get what you want (It's a shame that me is not one of your goals rsrs)... But, what more? Your fears, you perfect day, your Family.... </p>
            <p></p>
            <p>Tell me your Dirty secrets babe haha 📖</p>
            <p></p>
            <p>This week you go back to work né? Sooo that u have a good return 🙏🏽</p>
            <p></p>
            <p>kisses and hugs my boy 🥰😘</p>
            <p></p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
  
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image(
            "kiss.jpeg",
            caption="To u 😘",
            use_container_width =False, width=300,
        )


# Rodapé
st.write("---")
st.caption("Created with ❤️ using freetime")

#st.video("meu_video.mp4", start_time=10) 
