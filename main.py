# ---
from fasthtml.common import *
import uvicorn

app = FastHTML()
rt = app.route

# ---
page = Html(
            Head(
                Meta(charset='UTF-8'),
                Meta(name='viewport', content='width=device-width, initial-scale=1'),
                Title('LPテンプレート'),
                Meta(name='keywords', content=''),
                Meta(name='description', content=''),
                Link(rel='icon', type='image/png', href='img/favicon.png'),
                Link(rel='stylesheet', media='all', href='css/ress.min.css')(
                    Link(rel='stylesheet', media='all', href='css/style.css'),
                    Script(src='js/jquery-3.6.0.min.js'),
                    Script(src='js/style.js'),
                    Link(rel='icon', type='image/png', href='img/favicon.png')
                )
            ),
            Body(
                Header(
                    Div(cls='container')(
                        Div(cls='row')(
                            Div(cls='col span-12 header')(
                                H1(
                                    A('LOGO', href='')
                                ),
                                Div(cls='header-box')(
                                    A(href='')(
                                        Span('お問い合わせ', cls='contact-button')
                                    )
                                )
                            )
                        ),
                        Div(cls='row')(
                            Div(cls='col span-12')(
                                Nav(
                                    Div(id='open'),
                                    Div(id='close'),
                                    Div(id='navi')(
                                        Ul(
                                            Li(
                                                A('ホーム', href='index.html')
                                            ),
                                            Li(
                                                A('商品について', href='#1')
                                            ),
                                            Li(
                                                A('お客様の声', href='#2')
                                            ),
                                            Li(
                                                A('申し込みの流れ', href='#3')
                                            ),
                                            Li(
                                                A('アクセス', href='#4')
                                            ),
                                            Li(
                                                A('お問い合わせ', href='#5')
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                ),
                Div(cls='mainimg')(
                    Img(src='img/mainimg.jpg', alt='メイン画像')
                ),
                Main(
                    Div(cls='catch')(
                        H2(
                            Span('キャッチフレーズ', cls='under')
                        ),
                        P(
                            'ここにキャッチコピーが入ります。',
                            Br(),
                            'お店の宣伝やコンセプトなど。魅せる文言を入力。'
                        )
                    ),
                    Section(id='1', cls='gray-back')(
                        H2(cls='center')(
                            Span('商品について', cls='under')
                        ),
                        Div(cls='container center')(
                            Div(cls='row')(
                                Div(cls='col span-4')(
                                    Img(src='img/product.jpg', alt='ここに商品'),
                                    H3('ここに商品が入ります'),
                                    P('ここに説明文が入ります')
                                ),
                                Div(cls='col span-4')(
                                    Img(src='img/product.jpg', alt='ここに商品'),
                                    H3('ここに商品が入ります'),
                                    P('ここに説明文が入ります')
                                ),
                                Div(cls='col span-4')(
                                    Img(src='img/product.jpg', alt='ここに商品'),
                                    H3('ここに商品が入ります'),
                                    P('ここに説明文が入ります')
                                )
                            )
                        )
                    ),
                    Section(id='2')(
                        H2(cls='center')(
                            Span('スタッフ紹介', cls='under')
                        ),
                        Div(cls='container center')(
                            Div(cls='row')(
                                Div(cls='col span-4')(
                                    Img(src='img/staff.jpg', alt='スタッフ'),
                                    H3('スタッフ'),
                                    P('ここに説明文が入ります')
                                ),
                                Div(cls='col span-4')(
                                    Img(src='img/staff.jpg', alt='スタッフ'),
                                    H3('スタッフ'),
                                    P('ここに説明文が入ります')
                                ),
                                Div(cls='col span-4')(
                                    Img(src='img/staff.jpg', alt='スタッフ'),
                                    H3('スタッフ'),
                                    P('ここに説明文が入ります')
                                )
                            )
                        )
                    ),
                    Section(id='3', cls='gray-back')(
                        H2(cls='center')(
                            Span('申し込みの流れ', cls='under')
                        ),
                        Div(cls='container')(
                            Div(cls='row flow')(
                                Div(cls='col span-3')(
                                    Img(src='img/flow.jpg', alt='申し込み')
                                ),
                                Div(cls='col span-9')(
                                    P('ここに文章が入ります。ここに文章が入ります。ここに文章が入ります。')
                                )
                            ),
                            Div(cls='row flow')(
                                Div(cls='col span-3')(
                                    Img(src='img/flow.jpg', alt='申し込み')
                                ),
                                Div(cls='col span-9')(
                                    P('ここに文章が入ります。ここに文章が入ります。ここに文章が入ります。')
                                )
                            ),
                            Div(cls='row flow')(
                                Div(cls='col span-3')(
                                    Img(src='img/flow.jpg', alt='申し込み')
                                ),
                                Div(cls='col span-9')(
                                    P('ここに文章が入ります。ここに文章が入ります。ここに文章が入ります。')
                                )
                            )
                        )
                    ),
                    Section(id='4')(
                        H2(cls='center')(
                            Span('アクセス', cls='under')
                        ),
                        Div(cls='container')(
                            Div(cls='row')(
                                Div(cls='col span-12')(
                                    Iframe(src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d27814443.96425483!2d120.28897720705172!3d31.679877148840735!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x34674e0fd77f192f%3A0xf54275d47c665244!2z5pel5pys!5e0!3m2!1sja!2sjp!4v1555153587836!5m2!1sja!2sjp', width='100%', height='450', frameborder='0', style='border:0', allowfullscreen='')
                                )
                            )
                        )
                    ),
                    Section(id='5')(
                        H2(cls='center')(
                            Span('お問い合わせ', cls='under')
                        ),
                        Div(cls='container')(
                            Div(cls='row')(
                                Div(cls='col span-6')(
                                    Div(cls='contact-box')(
                                        P(
                                            Img(src='img/tel.png', alt='電話')
                                        ),
                                        P('012-345-6789')
                                    )
                                ),
                                Div(cls='col span-6')(
                                    Div(cls='contact-box')(
                                        P(
                                            Img(src='img/mail.png', alt='Eメール')
                                        ),
                                        P('simple@mail.com')
                                    )
                                )
                            ),
                            Div(cls='row')(
                                Div(cls='col span-12')(
                                    Form(method='post', action='')(
                                        Table(cls='table full-width')(
                                            Tbody(
                                                Tr(
                                                    Th(
                                                        Label('お名前', fr='name')
                                                    ),
                                                    Td(
                                                        Input(type='text', name='お名前', placeholder='名前を記入', id='exampNameInput', cls='full-width')
                                                    )
                                                ),
                                                Tr(
                                                    Th(
                                                        Label('メールアドレス', fr='email')
                                                    ),
                                                    Td(
                                                        Input(type='email', name='Email', placeholder='メールアドレスを記入', id='exampleEmailInput', cls='full-width')
                                                    )
                                                ),
                                                Tr(
                                                    Th(
                                                        Label('お電話番号', fr='tel')
                                                    ),
                                                    Td(
                                                        Input(type='tel', name='お電話番号', placeholder='お電話番号を記入', id='exampleTellInput', cls='full-width')
                                                    )
                                                ),
                                                Tr(
                                                    Th(
                                                        Label('お問い合わせ内容', fr='exampleMessage')
                                                    ),
                                                    Td(
                                                        Textarea(name='お問い合わせ内容', placeholder='用件をご記入ください …', id='exampleMessage', cls='full-width textarea')
                                                    )
                                                )
                                            )
                                        ),
                                        P(cls='center')(
                                            Input(type='submit', value='送 信', cls='button')
                                        )
                                    )
                                )
                            )
                        )
                    )
                ),
                Footer(
                    Div(cls='container')(
                        Div(cls='row')(
                            Div(cls='col span-4')(
                                H4('フッター1'),
                                P('ここにSNSやテキストなどが入ります。SNSやテキストなどが入ります。')
                            ),
                            Div(cls='col span-4')(
                                H4('フッター2'),
                                P('ここにSNSやテキストなどが入ります。SNSやテキストなどが入ります。')
                            ),
                            Div(cls='col span-4')(
                                H4('フッター3'),
                                P('ここにSNSやテキストなどが入ります。SNSやテキストなどが入ります。')
                            )
                        )
                    )
                ),
                Div(cls='copyright')(
                    A('Copyright © popodesign.', href='https://popo-design.net', target='_blank')
                ),
                P(id='pagetop')(
                    A('TOP', href='#')
                )
            )
        )

# ----
@rt("/")
def get():
    return page
  
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))