from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image 
import iminfo

app = Flask(__name__)
bootstrap = Bootstrap(app)
info3 = iminfo.image_info

def im_atr(imid, Ana, doc):
    filename = info3[Ana]['id']
    with Image.open(f'static/images/{filename}.jpg') as current:
        return {
            'image': imid,
            'file': doc,
            'attr': {
                'id': info3[Ana]['id'], 'title': info3[Ana]['title'],
            },
            'width': current.size[0],
            'height': current.size[1],
            'format': current.format,
            'mode': current.mode  
        }

def get_im(Ana):
    return{'id': info3[Ana]['id'], 'title': info3[Ana]['title']}


@app.route('/')
def home():
    return render_template('Ana.html',
     im1=get_im(0), 
     im2=get_im(1), 
     im3=get_im(2))

@app.route('/picture/<imid>')
def pic(imid):
    i1 = im_atr(imid, 0, 'first_image.html')
    i2 = im_atr(imid, 1, 'second_image.html')
    i3 = im_atr(imid, 2, 'third_image.html')
    if imid == i1['attr']['id']:
        return render_template(
            i1['file'], attr=i1['attr'], id=i1['image'], format=i1['format'],
            mode=i1['mode'],width=i1['width'], height=i1['height'])
    elif imid == i2['attr']['id']:
        return render_template(
            i2['file'], attr=i2['attr'], id=i2['image'], format=i2['format'],
            mode=i2['mode'],width=i2['width'], height=i2['height'])
    else:
        return render_template(
            i3['file'], attr=i3['attr'], id=i3['image'], format=i3['format'],
            mode=i3['mode'],width=i3['width'], height=i3['height'])