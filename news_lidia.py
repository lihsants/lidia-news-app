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
if st.button("Open your letter 💌"):
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

# Rodapé
st.write("---")
st.caption("Created with ❤️ using freetime")
