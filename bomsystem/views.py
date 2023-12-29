from flask import Blueprint, render_template, request, redirect, url_for
from .models import BOM
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_bom = BOM(
            request.form.get('part_number'),
            request.form.get('description'),
            request.form.get('quantity'),
            request.form.get('unit_measure'),
            request.form.get('material'),
            request.form.get('weight'),
            request.form.get('cost'),
            request.form.get('vendor_supplier'),
            request.form.get('lead_time'),
            request.form.get('revision_level'),
            request.form.get('assembly_code'),
            request.form.get('notes'),
        )

        db.session.add(new_bom)
        db.session.commit()
        print('Record successfully added')
        return redirect(url_for('views.displayAllBOMS'))

    return render_template('index.html')


@views.route('/all', methods=['GET', 'POST'])
def displayAllBOMS():
    if request.method == 'GET':
        bom = BOM.query.all()
        return render_template('all_data.html', boms=bom)


@views.route('/bom/delete/<int:id>', methods=['POST'])
def bom_delete(id):
    bom = BOM.query.get(id)
    if bom:
        msg_text = f'BOM {bom.bom_id} successfully removed'
        db.session.delete(bom)
        db.session.commit()
        print(msg_text)

        return redirect(url_for('views.displayAllBOMS'))
    

# @views.route('/bom/update/<int:id>', method=['POST'])
# def bom_update(id):
#     pass