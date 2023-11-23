from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import secrets

import os

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)
foo = secrets.token_urlsafe(16)
app.secret_key = foo

lims_user = os.environ['AIBS_LIMS_USER']
lims_pwd = os.environ['AIBS_LIMS_PWD']
lims_alias = os.environ['AIBS_LIMS_ALIAS']

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{lims_user}:{lims_pwd}@{lims_alias}/lims2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WTF_CSRF_ENABLED'] = False

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

class Specimen(db.Model):
    __tablename__ = 'specimens'
    id = db.Column(db.String)
    name = db.Column(db.String, primary_key = True)
    plane_of_section_id = db.Column(db.String)
    frozen_at = db.Column(db.String)
    rna_integrity_number = db.Column(db.String)
    tissue_ph = db.Column(db.Double)
    hemisphere_id = db.Column(db.String)
    created_by = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.String)
    structure_id = db.Column(db.String)
    postmortem_interval_id = db.Column(db.String)
    preparation_method_id = db.Column(db.String)
    parent_x_coord = db.Column(db.String)
    parent_y_coord = db.Column(db.String)
    parent_z_coord = db.Column(db.String)
    barcode = db.Column(db.String)
    location_id = db.Column(db.String)
    storage_directory = db.Column(db.String)
    project_id = db.Column(db.String)
    specimen_preparation_method_id = db.Column(db.String)
    alignment3d_id = db.Column(db.String)
    reference_space_id = db.Column(db.String)
    external_specimen_name = db.Column(db.String)
    normalization_group_id = db.Column(db.String)
    carousel_well_name = db.Column(db.String)
    donor_id = db.Column(db.String) 
    ephys_cell_plan_id = db.Column(db.String)
    ephys_roi_result_id = db.Column(db.String)
    histology_well_name = db.Column(db.String)
    priority = db.Column(db.String)
    ephys_neural_tissue_plan_id = db.Column(db.String)
    tissue_processing_id = db.Column(db.String)
    task_flow_id = db.Column(db.String)
    specimen_set_id = db.Column(db.String)
    biophysical_model_state = db.Column(db.String)
    cell_prep_id = db.Column(db.String)
    data = db.Column(db.String)
    cell_depth = db.Column(db.String)
    cell_reporter_id = db.Column(db.String)
    facs_well_id = db.Column(db.String)
    patched_cell_container = db.Column(db.String)
    cortex_layer_id = db.Column(db.String)
    cell_label = db.Column(db.String)
    flipped_specimen_id = db.Column(db.String)
    operation_id = db.Column(db.String)
    pinned_radius = db.Column(db.String)
    x_coord = db.Column(db.String)
    y_coord = db.Column(db.String)
    ephys_qc_result = db.Column(db.String)
    ephys_start_time_sec = db.Column(db.String)
    starter_cell_count = db.Column(db.String)
    task_id = db.Column(db.String)
    workflow_state = db.Column(db.String)
    mfish_experiment_id = db.Column(db.String)
    sectioning_task_id = db.Column(db.String)
    merscope_experiment_id = db.Column(db.String)
    oligo_tag = db.Column(db.String)
    parent_id = db.Column(db.String)

class Donor(db.Model):
    __tablename__ = "donors"
    id = db.Column(db.String)
    name = db.Column(db.String, primary_key = True)
    organism_id = db.Column(db.String)
    height = db.Column(db.String)
    weight = db.Column(db.String)
    gender_id = db.Column(db.String)
    race_id = db.Column(db.String)
    handedness_id = db.Column(db.String)
    education_level_id = db.Column(db.String)
    created_by = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.String)
    death_manner_id = db.Column(db.String)
    death_cause_id = db.Column(db.String)
    death_on = db.Column(db.String)  
    age_id = db.Column(db.String)
    external_donor_name = db.Column(db.String)
    induction_method = db.Column(db.String)
    transgenic_induction_method_id = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    primary_tissue_source_id = db.Column(db.String)
    baseline_weight_g = db.Column(db.String)
    data = db.Column(db.String)
    full_genotype = db.Column(db.String)
    occupation_id = db.Column(db.String)
    water_restricted = db.Column(db.String)

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.String, primary_key = True)
    jp2 = db.Column(db.String)
    zoom = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    qc_date = db.Column(db.String)
    slide_id = db.Column(db.String)
    width = db.Column(db.String)
    height = db.Column(db.String)
    image_type_id = db.Column(db.String)
    parent_id = db.Column(db.String)
    position = db.Column(db.String)
    specimen_id = db.Column(db.String)
    jp2_md5sum = db.Column(db.String)
    flip_id = db.Column(db.String)
    zoom_tiers = db.Column(db.String)
    archive_dir = db.Column(db.String)
    zoom_archive_dir = db.Column(db.String)
    treatment_id = db.Column(db.String)

class SpecimenTypes(db.Model):
    __tablename__ = 'specimen_types'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String) 
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

class Plane(db.Model):
    __tablename__ = 'plane_of_sections'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String) 
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

class ImageTypes(db.Model):
    __tablename__ = 'image_types'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String) 
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    reuploadable = db.Column(db.String)

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String) 
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    file_storage = db.Column(db.String)
    subdirectory_count = db.Column(db.String)
    current_directory = db.Column(db.String)
    trigger_dir = db.Column(db.String)
    failed_trigger_dir = db.Column(db.String)
    process_triggers = db.Column(db.String)
    incoming_directory = db.Column(db.String)
    non_cached_schema_name = db.Column(db.String)
    digital_archive_id = db.Column(db.String)

class Structure(db.Model):
    __tablename__ = 'structures'
    id = db.Column(db.String, primary_key = True)
    atlas_id = db.Column(db.String)
    name = db.Column(db.String)
    acronym = db.Column(db.String)
    red = db.Column(db.String)
    green = db.Column(db.String)
    blue = db.Column(db.String)
    st_order = db.Column(db.String)
    st_level = db.Column(db.String)
    ontology_id = db.Column(db.String)
    hemisphere_id = db.Column(db.String)
    sibling_order = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

class Age(db.Model):
    __tablename__ = 'ages'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    organism_id = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    days = db.Column(db.String)
    isembryonic = db.Column(db.String)

class Organism(db.Model):
    __tablename__ = 'organisms'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    ncbitaxonomyid = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    common_name = db.Column(db.String)

class SpecimenTypesSpecimens(db.Model):
    __tablename__ = 'specimen_types_specimens'
    specimen_type_id = db.Column(db.String)
    specimen_id = db.Column(db.String, primary_key = True)

class SubImage(db.Model):
    __tablename__ = "sub_images"
    id = db.Column(db.String, primary_key = True)
    image_id = db.Column(db.String)
    row = db.Column(db.String)
    x = db.Column(db.String)
    y = db.Column(db.String)
    width = db.Column(db.String)
    height = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    image_series_id = db.Column(db.String)
    failed = db.Column(db.String)
    specimen_id = db.Column(db.String)
    sub_image_qcstate_reason_id = db.Column(db.String)
    qc_date = db.Column(db.String)
    expression = db.Column(db.String)
    structure_id = db.Column(db.String)
    col = db.Column(db.String)
    specimen_tissue_index = db.Column(db.String)
    closest_nissl_sub_image_id = db.Column(db.String)
    area = db.Column(db.String)
    image_series_sub_image_index = db.Column(db.String)
    alignment2d_id = db.Column(db.String)
    sub_image_type_id = db.Column(db.String)
    bounding_box_index = db.Column(db.String)
    lims1_id = db.Column(db.String)
    svg_upload_msg = db.Column(db.String)

class Slide(db.Model):
    __tablename__ = "slides"
    id = db.Column(db.String, primary_key = True)
    barcode = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    run_group_slide_index = db.Column(db.String)
    slide_group_id = db.Column(db.String)
    slide_group_index = db.Column(db.String)
    slide_group_x_index = db.Column(db.String)
    slide_group_y_index= db.Column(db.String)
    qc_date = db.Column(db.String)
    run_group_id = db.Column(db.String)
    name = db.Column(db.String)
    run_plan_slide_index = db.Column(db.String)
    storage_directory = db.Column(db.String)
    scanner_id = db.Column(db.String)
    lims1_id = db.Column(db.String)
    ported_from_lims1 = db.Column(db.String)
    workflow_state = db.Column(db.String)
    slide_registration_state_id = db.Column(db.String)
    segmented = db.Column(db.String)
    parent_id = db.Column(db.String)
    slide_group_z_index = db.Column(db.String)

class ImageSeries(db.Model):
    __tablename__ = "image_series"
    id = db.Column(db.String, primary_key = True)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    position = db.Column(db.String)
    qc_date = db.Column(db.String)
    expression = db.Column(db.String)
    run_group_id = db.Column(db.String)
    specimen_id = db.Column(db.String)
    project_id = db.Column(db.String)
    published_at = db.Column(db.String)
    lims1_id = db.Column(db.String)
    storage_directory = db.Column(db.String)
    name = db.Column(db.String)
    workflow_state = db.Column(db.String)
    alignment3d_id = db.Column(db.String)
    equalization_id = db.Column(db.String)
    type = db.Column(db.String)
    is_stack = db.Column(db.String)
    archive_dir = db.Column(db.String)

class RunGroups(db.Model):
    __tablename__ = "run_groups"
    id = db.Column(db.String, primary_key = True)
    runplan_id = db.Column(db.String)
    run_group_type_id = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    name = db.Column(db.String)
    comments = db.Column(db.String)
    qc_date = db.Column(db.String)
    run_group_state_id = db.Column(db.String)
    lims1_id = db.Column(db.String)
    workflow_state = db.Column(db.String)
    treatment_id = db.Column(db.String)

class Treatment(db.Model):
    __tablename__ = "treatments"
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    public = db.Column(db.String)

class DonorForm(FlaskForm):
    donor = StringField('What is the name of the donor you would like to see?', validators=[DataRequired(), Length(1, 40)])
    submit = SubmitField('Submit')

class Node:
    def __init__ (self, name, children=None):
        self.name = name 
        self.children = children if children is not None else []

        specimen = Specimen.query.filter_by(name=name).first()
        specimen_type = SpecimenTypesSpecimens.query.filter_by(specimen_id=specimen.id).first()
        specimen_type_name = "None"
        if specimen_type:
            specimen_type_name = SpecimenTypes.query.filter_by(id=specimen_type.specimen_type_id).first().name
            self.name = str(self.name) + ": " + str(specimen_type_name)

        self.has_image = False
        if Image.query.filter_by(specimen_id=specimen.id).first() or (SubImage.query.filter_by(specimen_id=specimen.id).first() and specimen_type_name != "Cell"):
            self.has_image = True

# asks the user to enter the donor they want to see the data for
@app.route('/', methods=['GET', 'POST'])
def home():
    possible_donors = []
    message = ""

    form = DonorForm()
    if form.validate_on_submit():
        donor_name = form.donor.data

        # gets the donor that matches the requested donor id
        donor = Donor.query.filter_by(name = donor_name).first()

        if donor is None:
            donor = Donor.query.filter_by(name = donor_name.upper()).first()

        if donor is not None:
            form.donor.data = ""

            # goes to appropriate specimen page based on donor id 
            # calls specimen method
            return redirect(url_for('specimens', donor_name=donor.name))
        else:
            donors = Donor.query.order_by(Donor.name).all()
            for donor in donors:
                if donor.name.startswith(donor_name):
                    possible_donors.append(donor.name)
            message = "That donor is not in our database"

    return render_template('home.html', form=form, message=message, possible_donors=possible_donors)

# builds the parent-child relationship between specimens 
# generates dropdown menu with hierarchy built in through flattened data
@app.route('/specimens/<donor_name>/')
def specimens(donor_name):

    donor_id = Donor.query.filter_by(name = donor_name).first().id

    # get table of specimens matching given donor id (has all columns!)
    specimens = Specimen.query.filter_by(donor_id=donor_id).order_by(Specimen.name)

    # provides the metadata for the first specimen in the specimen list for the requested donor 
    # makes it so that the starting metadata display is the root specimen 
    specimen_data = populate_metadata(specimens.first().name)

    tree = build_tree(specimens)

    # renders template that displays all specimens in table with their id and parent id
    return render_template('dropdown_and_metadata.html', tree = tree, specimen_data = specimen_data)

# specimens = table of all specimens with given donor_id
# maps specimen ids to children
def build_tree(specimens):
    def build_node(name):
        return Node(name, [build_node(child) for child in relationships.get(name, [])])
    
    relationships = {}
    root_names = []

    for specimen in specimens:
        parent_id = specimen.parent_id
        if parent_id:
            parent_name = Specimen.query.filter_by(id=specimen.parent_id).first().name
            if parent_name not in relationships:
                relationships[parent_name] = []
            relationships[parent_name].append(specimen.name)
        else:
            root_names.append(specimen.name)
    
    trees = [build_node(root) for root in root_names]
    
    return trees

# gets all of the relevant metadata for the given specimen
def populate_metadata(specimen_name):
    # gets the specimen name without the specimen_type after it if applicable 
    specimen_name = specimen_name.split(":", 1)[0]
    specimen = Specimen.query.filter_by(name=specimen_name).first()

    specimen_data = {
        'id': specimen.id,
        'name': specimen.name, 
        'donor_id': specimen.donor_id,
        'parent_x_coord': specimen.parent_x_coord,
        'parent_y_coord': specimen.parent_y_coord,
        'parent_z_coord': specimen.parent_z_coord,
        'parent_id': "None",
        'storage_directory': "None",
        'plane_of_section': "None",
        'project_name': "None", 
        'structure': "None",
        'parent_name': "None",
        'specimen_type': "None",
        'age': "None",
        'organism': "None",
        'image_types': [],
        'image_names': [],
        'image_urls': [],
        'sub_image_names': [],
        'sub_image_storage_directory': [],
        'treatment': {}, 
        'all_image_names': []
    }
    
    if specimen.parent_id:
        specimen_data['parent_id'] = specimen.parent_id
        specimen_data['parent_name'] = Specimen.query.filter_by(id=specimen.parent_id).first().name
    
    if specimen.plane_of_section_id: 
        specimen_data['plane_of_section'] = Plane.query.filter_by(id=specimen.plane_of_section_id).first().name
    
    if specimen.project_id:
        specimen_data['project_name'] = Project.query.filter_by(id=specimen.project_id).first().name
    
    if specimen.structure_id:
        specimen_data['structure'] = Structure.query.filter_by(id=specimen.structure_id).first().name

    donor = Donor.query.filter_by(id=specimen.donor_id).first()
    if donor.age_id:
        specimen_data['age'] = Age.query.filter_by(id=donor.age_id).first().name
    
    if donor.organism_id:
        specimen_data['organism'] = Organism.query.filter_by(id=donor.organism_id).first().common_name
    
    specimen_type = SpecimenTypesSpecimens.query.filter_by(specimen_id=specimen.id).first()
    if specimen_type:
        specimen_data['specimen_type'] = SpecimenTypes.query.filter_by(id=specimen_type.specimen_type_id).first().name
    
    if specimen.storage_directory:
        specimen_data['storage_directory'] = specimen.storage_directory

    # checks for presence of single image
    if Image.query.filter_by(specimen_id=specimen.id).first():
        images = Image.query.filter_by(specimen_id=specimen.id)
        for image in images:
            specimen_data['image_types'].append(" " + ImageTypes.query.filter_by(id=image.image_type_id).first().name)
            specimen_data['all_image_names'].append(image.zoom)
            specimen_data['image_names'].append(" " + image.zoom)
            image_url = str(convert_aff("//" + str(specimen_data['storage_directory'] + image.zoom), image))
            specimen_data['image_urls'].append(image_url)

            # there will never be a treatment associated with these types of images
            specimen_data['treatment'][image_url] = "None"
    else:
        specimen_data['image_types'] = "None"
        specimen_data['image_names'] = "None"

    # need to make sure the type isn't "Cell" bc there are dozens of sub-images of cells that aren't needed
    sub_images = SubImage.query.filter_by(specimen_id=specimen.id)
    has_sub_image = False
    if sub_images and specimen_data['specimen_type'] != "Cell":
        for sub_image in sub_images:
            image = Image.query.filter_by(id=sub_image.image_id).first()
            slide = Slide.query.filter_by(id=image.slide_id).first()
            if slide:
                has_sub_image = True
                storage_dir = slide.storage_directory

                # will only add the storage_directory to the list if it's not already in it
                if (" " + storage_dir) not in specimen_data['sub_image_storage_directory']:
                    specimen_data['sub_image_storage_directory'].append(" " + storage_dir)
                    
                specimen_data['sub_image_names'].append(" " + image.zoom)
                specimen_data['all_image_names'].append(image.zoom)

                image_url = str(convert_aff("//" + str(storage_dir + image.zoom), sub_image))
                specimen_data['image_urls'].append(image_url)

                # series of checks and joins to get to the treatment for each sub_image
                image_series = ImageSeries.query.filter_by(id=sub_image.image_series_id).first()
                if image_series:
                    run_group = RunGroups.query.filter_by(id=image_series.run_group_id).first()
                    if run_group:
                        treatment = Treatment.query.filter_by(id=run_group.treatment_id).first()
                        if treatment:
                            # maps the image url to the corresponding treatment
                            specimen_data['treatment'][image_url] = treatment.name
                        else:
                            specimen_data['treatment'] = "None"
    
    # makes these keys None if there are no sub_images with a storage_directory associated with them
    if not has_sub_image:
        specimen_data['sub_image_names'] = "None"
        specimen_data['sub_image_storage_directory'] = "None"
        if len(specimen_data['image_urls']) == 0:
            specimen_data['image_urls'] = "None"

    return specimen_data

# creates the image url for an .aff image so it can be rendered in html
def convert_aff(img_path, image):
    new_url = 'http://lims2/cgi-bin/imageservice?mime=2&path=' 
    new_url += str(img_path)
    new_url += '&top=0&left=0&width='
    new_url += str(image.height)
    new_url += '&zoom='
    new_url += str(5)

    return new_url

# reroutes the page to update the metadata based on which specimen the user clicks in the dropdown menu
# makes it so that the state of the dropdown menu doesn't change as you click through it
@app.route('/get_specimen_data', methods=['POST'])
def get_specimen_data():
    data= request.get_json()
    node_name = data.get('node_name')
    specimen_data = populate_metadata(node_name)
    return jsonify(specimen_data)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
