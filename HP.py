from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image 
import im_info
import image_info
import iminfo

app = Flask(__name__)
bootstrap = Bootstrap(app)
info = im_info.image_info
info2 = image_info.image_info
info3 = iminfo.image_info

def im_atr(imid, Jose, doc):
    filename = info[Jose]['id']
    with Image.open(f'static/images/{filename}.jpg') as current:
        return {
            'image': imid,
            'file': doc,
            'attr': {
                'id': info[Jose]['id'], 'title': info[Jose]['title'],
            },
            'width': current.size[0],
            'height': current.size[1],
            'format': current.format,
            'mode': current.mode  
        }

def im_atr2(imid, vandit, doc):
    filename = info2[vandit]['id']
    with Image.open(f'static/images/{filename}.jpg') as current:
        return {
            'image': imid,
            'file': doc,
            'attr': {
                'id': info2[vandit]['id'], 'title': info2[vandit]['title'],
            },
            'width': current.size[0],
            'height': current.size[1],
            'format': current.format,
            'mode': current.mode  
        }

def im_atr3(imid, Ana, doc):
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

def get_im(Jose):
    return{'id': info[Jose]['id'], 'title': info[Jose]['title']}

def get_im2(vandit):
    return{'id': info2[vandit]['id'], 'title': info2[vandit]['title']}

def get_im3(Ana):
    return{'id': info3[Ana]['id'], 'title': info3[Ana]['title']}

@app.route('/')
def home():
    return render_template('index.html',
     im1=get_im(0), 
     im2=get_im2(0), 
     im3=get_im3(0))

@app.route('/picture/<imid>')
def pic(imid):
    i1 = im_atr(imid, 0, 'firm.html')
    i2 = im_atr2(imid, 0, 'fim.html')
    i3 = im_atr3(imid, 0, 'first_image.html')
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

@app.route('/page2')
def page2func():
    return render_template('Jose.html',
     im1=get_im(0), 
     im2=get_im(1), 
     im4=get_im(2))

@app.route('/picture/<imid2>')
def pic2(imid2):
    i1 = im_atr(imid2, 0, 'firm.html')
    i2 = im_atr(imid2, 1, 'secim.html')
    i3 = im_atr(imid2, 2, 'thim.html')
    if imid2 == i1['attr']['id']:
        return render_template(
            i1['file'], attr=i1['attr'], id=i1['image'], format=i1['format'],
            mode=i1['mode'],width=i1['width'], height=i1['height'])
    elif imid2 == i2['attr']['id']:
        return render_template(
            i2['file'], attr=i2['attr'], id=i2['image'], format=i2['format'],
            mode=i2['mode'],width=i2['width'], height=i2['height'])
    else:
        return render_template(
            i3['file'], attr=i3['attr'], id=i3['image'], format=i3['format'],
            mode=i3['mode'],width=i3['width'], height=i3['height'])

@app.route('/page3')
def page3func():
    return render_template('vandit.html',
     im1=get_im2(0), 
     im2=get_im2(1), 
     im3=get_im2(2))

@app.route('/picture/<imid3>')
def pic3(imid3):
    i1 = im_atr2(imid3, 0, 'fim.html')
    i2 = im_atr2(imid3, 1, 'sim.html')
    i3 = im_atr2(imid3, 2, 'tim.html')
    if imid3 == i1['attr']['id']:
        return render_template(
            i1['file'], attr=i1['attr'], id=i1['image'], format=i1['format'],
            mode=i1['mode'],width=i1['width'], height=i1['height'])
    elif imid3 == i2['attr']['id']:
        return render_template(
            i2['file'], attr=i2['attr'], id=i2['image'], format=i2['format'],
            mode=i2['mode'],width=i2['width'], height=i2['height'])
    else:
        return render_template(
            i3['file'], attr=i3['attr'], id=i3['image'], format=i3['format'],
            mode=i3['mode'],width=i3['width'], height=i3['height'])

@app.route('/page4')
def page4func():
    return render_template('Ana.html',
     im1=get_im3(0), 
     im2=get_im3(1), 
     im3=get_im3(2))
