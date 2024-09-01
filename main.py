# ---
from fasthtml.common import *
#import uvicorn

# ---
page = Html(
            Head(
                Meta(charset='UTF-8'),
                Meta(name='viewport', content='width=device-width, initial-scale=1'),
                Title('LPテンプレート'),
                Meta(name='keywords', content=''),
                Meta(name='description', content=''),
                Link(rel='icon', type='image/png', href='img/favicon.png')
            ),
            Body(
                Header(
                    Div(cls='container')(
                        Div(cls='row')(
                            Div(cls='col span-12 header')(
                                H1(
                                    A('LOGO')
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
                        )
                    ),
                    Section(id='2')(
                        H2(cls='center')(
                            Span('スタッフ紹介', cls='under')
                        )
                    ),
                    Section(id='3', cls='gray-back')(
                        H2(cls='center')(
                            Span('申し込みの流れ', cls='under')
                        )
                    ),
                    Section(id='4')(
                        H2(cls='center')(
                            Span('アクセス', cls='under')
                        )
                    ),
                    Section(id='5')(
                        H2(cls='center')(
                            Span('お問い合わせ', cls='under')
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
                )
            )
        )

# ---
#print(to_xml(page))

# ---
app,rt = fast_app()

@rt('/')
def get(): return page
  
serve()