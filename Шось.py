import streamlit as st
import base64
# Налаштування сторінки
st.set_page_config(page_title="З днем народження!", page_icon="💐")
# Функція для встановлення фону
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded_img = base64.b64encode(data).decode()

    # Визначаємо тип файлу для CSS
    file_extension = image_file.split(".")[-1].lower()
    mime_type = "image/png" if file_extension == "png" else "image/jpeg"

    css_code = f"""
    <style>
    .stApp {{
        background-image: url("data:{mime_type};base64,{encoded_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)


# Викликаємо функцію (замініть назву на вашу)
set_background("../PythonProject/background.png")



# Функція для кодування файлів у Base64, щоб браузер міг їх прочитати напряму з коду




# Створюємо стан додатка, щоб зберігати введені дані між перемиканнями сторінок
if "page" not in st.session_state:
    st.session_state.page = 1
if "dream" not in st.session_state:
    st.session_state.dream = ""
if "wish" not in st.session_state:
    st.session_state.wish = ""

# --- СТОРІНКА 1: Введення імені ---
if st.session_state.page == 1:
    st.title("Привіт Маріє! ✨")
    st.markdown(f"""
    ### Я - *чарівна відкритка*🔮  
    
    Я тут щоб привітати тебе і дозволити тобі попригадувати тобі моменти цього року :)  
    
    Коли будеш готова, натискай на кнопку знизу.  
    
    P.S: мій творець не побачить відповіді, тому пиши, все що спаде тобі на думку
    """)
    if st.button("Почнімо!"):
        st.session_state.page=2
        st.rerun()


# --- СТОРІНКА 2: Введення побажання або вибору ---
elif st.session_state.page == 2:
    st.title("Познайомимось!")
    st.markdown(f"Розкажи про свій рік!")

    wish_input = st.text_area("Що в твоєму році було для тебе приємним, принесло тобі радість?", key="my_secret_input")
    is_input_empty = st.session_state.my_secret_input.strip() == ""

    if st.button("Далі ->", disabled=is_input_empty):
        st.session_state.page=3
        st.rerun()

elif st.session_state.page == 3:
    st.title("Продовжимо!")

    wish_input = st.text_area("Що в твоєму році було непростим, викликало в тебе занепокоєння?", key="my_secret_input2")
    is_input_empty = st.session_state.my_secret_input2.strip() == ""

    if st.button("Далі ->", disabled=is_input_empty):
        st.session_state.page=4
        st.rerun()
elif st.session_state.page == 4:
    st.title("Перерва")


    def get_base64_file(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


    st.markdown("""Ти чудово йдеш! Саме час відновитися.  
      
    # Поклікай на цього сертифікованого котика-терапевта 🐾""")

    try:
        # Кодуємо кота та звук (замініть назви файлів на свої, якщо вони інші)
        cat_base64 = get_base64_file("../PythonProject/catimage.png")
        audio_base64 = get_base64_file("../PythonProject/catsound.mp3")

        # Створюємо HTML-код із вбудованим JavaScript для відтворення звуку при кліку
        html_code = f"""
        <div style="text-align: center;">
            <!-- Приховані аудіо-теги зі звуком нявкання -->
            <audio id="meow-sound">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>

            <!-- Клікабельне зображення кота -->
            <img src="data:image/png;base64,{cat_base64}" 
                 alt="Кіт" 
                 style="cursor: pointer; width: 250px; transition: transform 0.2s;" 
                 onclick="document.getElementById('meow-sound').play();"
                 onmousedown="this.style.transform='scale(0.95)';"
                 onmouseup="this.style.transform='scale(1)';"
                 onmouseleave="this.style.transform='scale(1)';"
            />
            <p style="color: gray; font-size: 14px; margin-top: 10px;">(Увімкни звук!)</p>
        </div>
        """

        # Виводимо HTML у Streamlit
        st.components.v1.html(html_code, height=350)
    except FileNotFoundError:
        st.error("Помилка: Переконайся, що файли 'catimage.png' та 'catsound.mp3' лежать в одній папці з цим скриптом!")
    if st.button("Йти далі"):
        st.session_state.page=5
        st.rerun()
elif st.session_state.page == 5:
    st.title("Твої побажання! ✨")
    st.write("Передивляючись свої спогади, чого б ти хотіла побажати собі найбільше?")
    wish_input=st.text_input("(Тільки для найщиріших побажань)", value=st.session_state.wish,key="my_secret_input3")
    is_input_empty = st.session_state.my_secret_input3.strip() == ""

    col1, col2 = st.columns(2)
    with col1:
        if st.button("<- Назад"):
            st.session_state.page = 4
            st.rerun()
    with col2:
        if st.button("Далі ->", disabled=is_input_empty):
            st.session_state.wish=wish_input
            st.session_state.page = 6
            st.rerun()
elif st.session_state.page == 6:
    st.title("Твої мрії! 🌟")
    st.write("Обери щось, чого б ти хотіла для себе в майбутньому (будь що: просте, фантастичне, абстрактне...)")
    dream_input=st.text_input("(Для твоїх мрій, що збудуться)", value= st.session_state.dream, key="my_secret_input4")
    is_input_empty = st.session_state.my_secret_input4.strip() == ""
    col1, col2 = st.columns(2)
    with col1:
        if st.button("<- Назад"):
            st.session_state.page = 5
            st.rerun()
    with col2:
        if st.button("Отримати відкритку", disabled=is_input_empty):
            st.session_state.dream = dream_input
            st.session_state.page = 7
            st.rerun()

# --- СТОРІНКА 3: Фінальний текст (Відкриточка) ---
elif st.session_state.page == 7:
    st.balloons()  # Святкова анімація з кульками!
    st.title("❤️ Твоя особлива відкриточка")

    # Головний текст листівки
    st.markdown(f"""
    ### Дорога **Маріє**,

    З днем народження тебе!
    Я сподіваюсь, що цей день приніс тобі радість, тепло і енергію.
    Ти написала, що бажаєш собі: *"{st.session_state.wish}"*. 
    Я також бажаю тобі цього і знаю, що це важливо для тебе.  
    Я чую і твої мрії: "{st.session_state.dream}".  
    Нехай тим чи іншим чином вони здійсняться.
    

    Дякую, що ти є. Бережи себе. ✨
    """)


