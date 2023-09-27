import psycopg2
from flask import Flask, render_template, request


def average(p):
    if len(p) == 0:
        return 0
    return round(sum(p) / len(p), 2)


app = Flask('Amazing school app')

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="school",      # change with your local user
    password="school")  # change with your local password


@app.route('/')
@app.route('/home/')
def show_home():
    """Shows the home template"""

    return render_template('home.html')


@app.route('/students/')
def show_students():
    """Show all the students"""

    with conn:
        query = """
            select 
                s.id, concat(s.last_name, ' ', s.first_name), 
                c.id, concat(c.class_number, c.class_letter) 
            from student s
            join "class" c on s.class_id = c.id 
            order by s.last_name;
        """
        c = conn.cursor()
        c.execute(query)
        records = c.fetchall()

    return render_template('students.html',
                           title='Elevii scolii noastre',
                           students=records)


@app.route('/student/<int:student_id>/')
def show_student(student_id):
    """Show the student with the given student_id"""

    with conn:
        query = """
            select 
                s.id, s.last_name, s.first_name, 
                c.id, concat(c.class_number, c.class_letter) 
            from student s
            join "class" c on s.class_id = c.id 
            where s.id = %s::integer;
        """
        c = conn.cursor()
        c.execute(query, (student_id,))
        record = c.fetchone()
        if record:
            title = f'{record[1]} {record[2]}'
        else:
            title = 'Elev inexistent'
    return render_template('student.html',
                           title=title,
                           student=record)


@app.route('/search/', methods=['GET', 'POST'])
def search_students():
    """Search the students for a given name"""

    if request.method == 'POST':
        srch = request.form
    else:
        srch = request.args

    search = srch.get('search').strip()

    with conn:
        query = """
            select 
                s.id, concat(s.last_name, ' ', s.first_name), 
                c.id, concat(c.class_number, c.class_letter) 
            from student s
            join "class" c on s.class_id = c.id 
            where s.first_name like %s or s.last_name like %s;
        """

        c = conn.cursor()
        c.execute(query, (f'%{search}%', f'%{search}%'))
        records = c.fetchall()

    return render_template('students.html',
                           title='Elevii scolii noastre',
                           students=records,
                           search=search)


@app.route('/classes/')
def show_classes():
    """Show all the classes"""

    with conn:
        query = """
            select id, concat(class_number, class_letter) 
            from "class"
            order by class_number, class_letter;
        """
        c = conn.cursor()
        c.execute(query)
        records = c.fetchall()

    return render_template('classes.html', classes=records)


@app.route('/class/<int:class_id>/')
def show_class(class_id):
    """Show the class with the given class_id"""

    with conn:
        query = """
            select 
                s.id, concat(s.last_name, ' ', s.first_name), 
                concat(c.class_number, c.class_letter) 
            from student s
            join "class" c on s.class_id = c.id 
            where c.id = %s::integer;
        """
        c = conn.cursor()
        c.execute(query, (class_id,))
        records = c.fetchall()
        if records:
            class_name = records[0][2]
        else:
            class_name = None

    return render_template('class.html', students=records, class_name=class_name, title='Clasa ' + class_name)


@app.route('/contact/')
def contact():
    """Display contact form"""
    return render_template('contact.html', title='Contact')


@app.errorhandler(404)
def page_not_found(e):
    """Catch inexistent routes"""
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
