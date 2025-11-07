from flask import render_template, request, redirect, url_for, session
from flask_babel import _
from flask_socketio import emit
from unit_converter import app, socketio
from unit_converter.length import convert_length
from unit_converter.mass import convert_mass
from unit_converter.pressure import convert_pressure
from unit_converter.area import convert_area
from unit_converter.data_storage import convert_data_storage
from unit_converter.energy import Convert_energy
from unit_converter.speed import Convert_speed
from unit_converter.temperature import Convert_temperature
from unit_converter.timec import Convert_time
from unit_converter.volume import Convert_volume
from unit_converter.urlcode import url_encode, url_decode
from unit_converter.base64code import base64_encode, base64_decode

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
@app.route("/Home")
def home():
    return render_template('index.html')

@app.route("/set_language", methods=['POST'])
def set_language():
    lang = request.form.get('language', 'en')
    if lang in app.config['LANGUAGES']:
        session['language'] = lang
    return redirect(request.referrer or url_for('home'))


@app.route("/area")
def area():
    return render_template('area.html')

@socketio.on('convert_area')
def handle_area_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = convert_area(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/data-storage")
def data_storage():
    return render_template('data_storage.html')

@socketio.on('convert_data_storage')
def handle_data_storage_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = convert_data_storage(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/energy")
def energy():
    return render_template('energy.html')

@socketio.on('convert_energy')
def handle_energy_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = Convert_energy(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/length")
def length():
    return render_template('length.html')

@socketio.on('convert_length')
def handle_length_conversion(data):
    try:
        from_unit = data['from_unit']
        to_unit = data['to_unit']
        from_value = float(data['from_value'])
        desc_result, short_result = convert_length(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/mass")
def mass():
    return render_template('mass.html')

@socketio.on('convert_mass')
def handle_mass_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = convert_mass(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/pressure")
def pressure():
    return render_template('pressure.html')

@socketio.on('convert_pressure')
def handle_pressure_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = convert_pressure(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/speed")
def speed():
    return render_template('speed.html')

@socketio.on('convert_speed')
def handle_speed_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = Convert_speed(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/temperature")
def temperature():
    return render_template('temperature.html')

@socketio.on('convert_temperature')
def handle_temperature_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = Convert_temperature(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/time")
def time():
    return render_template('time.html')

@socketio.on('convert_time')
def handle_time_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = Convert_time(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/urlcode")
def urlcode():
    return render_template('urlcode.html')

@socketio.on('url_encode')
def handle_url_encode(data):
    try:
        text = data.get('text', '')
        desc_result, short_result = url_encode(text, _)
        emit('urlcode_result', {
            'success': True,
            'result': short_result,
            'desc_result': desc_result
        })
    except Exception as e:
        error_msg = _('An error occurred during encoding')
        emit('urlcode_result', {
            'success': False,
            'error': error_msg
        })

@socketio.on('url_decode')
def handle_url_decode(data):
    try:
        text = data.get('text', '')
        desc_result, short_result = url_decode(text, _)
        emit('urlcode_result', {
            'success': True,
            'result': short_result,
            'desc_result': desc_result
        })
    except Exception as e:
        error_msg = _('An error occurred during decoding')
        emit('urlcode_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/base64code")
def base64code():
    return render_template('base64code.html')

@socketio.on('base64_encode')
def handle_base64_encode(data):
    try:
        text = data.get('text', '')
        desc_result, short_result = base64_encode(text, _)
        emit('base64code_result', {
            'success': True,
            'result': short_result,
            'desc_result': desc_result
        })
    except Exception as e:
        error_msg = _('An error occurred during encoding')
        emit('base64code_result', {
            'success': False,
            'error': error_msg
        })

@socketio.on('base64_decode')
def handle_base64_decode(data):
    try:
        text = data.get('text', '')
        desc_result, short_result = base64_decode(text, _)
        emit('base64code_result', {
            'success': True,
            'result': short_result,
            'desc_result': desc_result
        })
    except Exception as e:
        error_msg = _('An error occurred during decoding')
        emit('base64code_result', {
            'success': False,
            'error': error_msg
        })

@app.route("/volume")
def volume():
    return render_template('volume.html')

@socketio.on('convert_volume')
def handle_volume_conversion(data):
    try:
        from_unit = int(data['from_unit'])
        to_unit = int(data['to_unit'])
        from_value = float(data['from_value'])
        desc_result, short_result = Convert_volume(from_unit, to_unit, from_value, _)
        emit('conversion_result', {
            'success': True,
            'desc_result': desc_result,
            'short_result': short_result
        })
    except Exception as e:
        error_msg = _('An error occurred during conversion')
        emit('conversion_result', {
            'success': False,
            'error': error_msg
        })
