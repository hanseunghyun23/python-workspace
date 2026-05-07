import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = """
Python machine learning data science artificial intelligence
deep learning neural network programming code development
algorithm model training dataset feature engineering
"""



    def 실습2():
        wc = WordCloud(
            font_path = 'C:/Windows/Fonts/malgun.ttf',
            width=800,
            height=400,
            background_color='white',
            max_words=100,
            colormap='plasma'


        ).generate(text)

        # TODO: figure 사이즈 (10, 5)
        plt.figure(figsize=(10,5))

    # TODO: wc 이미지 출력, 보간법 bilinear
        plt.imshow(wc,interpolation='bilinear')

    # TODO: 축 끄기
        plt.axis('off')
        # TODO: 여백 자동조정
        plt.tight_layout()
        # TODO: 'wordcloud.png' 로 저장, dpi=150
        plt.savefig('wordcloud.png',dpi=150)
        # TODO: 화면에 출력
        plt.show()