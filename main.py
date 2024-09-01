#from fasthtml.common import *

#app, rt = fast_app()


#@rt("/")
#def get():
#    return Div(P("Hello World!"), hx_get="/change")

#serve()

# ---
from fasthtml.common import *
import uvicorn

app = FastHTML()
rt = app.route

@rt("/")
def get():
    return Title("FastHTML"), H1("Hello World!")
  
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))