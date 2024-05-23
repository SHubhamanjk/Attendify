from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Define the holidays (previously mentioned holidays will be hardcoded here)
holidays = [
    datetime.datetime(2023, 1, 26),
    datetime.datetime(2023, 2, 18),
    datetime.datetime(2023, 3, 6),
    datetime.datetime(2023, 3, 7),
    datetime.datetime(2023, 3, 8),
    datetime.datetime(2023, 3, 9),
    datetime.datetime(2023, 3, 10),
    datetime.datetime(2023, 3, 11),
    datetime.datetime(2023, 3, 29),
    datetime.datetime(2023, 3, 30),
    datetime.datetime(2023, 4, 14),
    datetime.datetime(2023, 4, 22),
    datetime.datetime(2023, 4, 29),
    datetime.datetime(2023, 5, 1),
    datetime.datetime(2023, 5, 5),
    datetime.datetime(2023, 6, 1),
    datetime.datetime(2023, 6, 2),
    datetime.datetime(2023, 6, 3),
    datetime.datetime(2023, 6, 5),
    datetime.datetime(2023, 6, 6),
    datetime.datetime(2023, 6, 7),
    datetime.datetime(2023, 6, 8),
    datetime.datetime(2023, 6, 9),
    datetime.datetime(2023, 6, 10),
    datetime.datetime(2023, 6, 12),
    datetime.datetime(2023, 6, 13),
    datetime.datetime(2023, 6, 14),
    datetime.datetime(2023, 6, 15),
    datetime.datetime(2023, 6, 16),
    datetime.datetime(2023, 6, 17),
    datetime.datetime(2023, 6, 19),
    datetime.datetime(2023, 6, 20),
    datetime.datetime(2023, 6, 22),
    datetime.datetime(2023, 6, 23),
    datetime.datetime(2023, 6, 24),
    datetime.datetime(2023, 6, 26),
    datetime.datetime(2023, 6, 27),
    datetime.datetime(2023, 6, 28),
    datetime.datetime(2023, 6, 29),
    datetime.datetime(2023, 6, 30),
    datetime.datetime(2023, 7, 29),
    datetime.datetime(2023, 8, 15),
    datetime.datetime(2023, 8, 30),
    datetime.datetime(2023, 9, 6),
    datetime.datetime(2023, 9, 28),
    datetime.datetime(2023, 10, 2),
    datetime.datetime(2023, 10, 21),
    datetime.datetime(2023, 10, 23),
    datetime.datetime(2023, 10, 24),
    datetime.datetime(2023, 10, 25),
    datetime.datetime(2023, 11, 10),
    datetime.datetime(2023, 11, 11),
    datetime.datetime(2023, 11, 13),
    datetime.datetime(2023, 11, 14),
    datetime.datetime(2023, 11, 15),
    datetime.datetime(2023, 11, 16),
    datetime.datetime(2023, 11, 17),
    datetime.datetime(2023, 11, 18),
    datetime.datetime(2023, 11, 20),
    datetime.datetime(2023, 11, 23),
    datetime.datetime(2023, 11, 21),
    datetime.datetime(2023, 11, 22),
    datetime.datetime(2023, 11, 27),
    datetime.datetime(2023, 12, 25),
    datetime.datetime(2023, 12, 26),
    datetime.datetime(2023, 12, 27),
    datetime.datetime(2023, 12, 28),
    datetime.datetime(2023, 12, 29),
    datetime.datetime(2023, 12, 30),
    datetime.datetime(2024, 1, 1),
    datetime.datetime(2024, 1, 15),
    datetime.datetime(2024, 1, 17),
    datetime.datetime(2024, 1, 26),
    datetime.datetime(2024, 2, 14),
    datetime.datetime(2024, 2, 24),
    datetime.datetime(2024, 2, 26),
    datetime.datetime(2024, 3, 22),
    datetime.datetime(2024, 3, 25),
    datetime.datetime(2024, 3, 26),
    datetime.datetime(2024, 3, 27),
    datetime.datetime(2024, 3, 28),
    datetime.datetime(2024, 3, 29),
    datetime.datetime(2024, 4, 12),
    datetime.datetime(2024, 4, 17),
    datetime.datetime(2024, 4, 23),
    datetime.datetime(2024, 5, 1),
    datetime.datetime(2024, 5, 23),
    datetime.datetime(2024, 7, 17),
    datetime.datetime(2024, 8, 15),
    datetime.datetime(2024, 8, 19),
    datetime.datetime(2024, 8, 26),
    datetime.datetime(2024, 9, 16),
    datetime.datetime(2024, 10, 2),
    datetime.datetime(2024, 10, 9),
    datetime.datetime(2024, 10, 10),
    datetime.datetime(2024, 10, 11),
    datetime.datetime(2024, 10, 12),
    datetime.datetime(2024, 10, 30),
    datetime.datetime(2024, 10, 31),
    datetime.datetime(2024, 11, 1),
    datetime.datetime(2024, 11, 2),
    datetime.datetime(2024, 11, 4),
    datetime.datetime(2024, 11, 5),
    datetime.datetime(2024, 11, 6),
    datetime.datetime(2024, 11, 7),
    datetime.datetime(2024, 11, 8),
    datetime.datetime(2024, 11, 9),
    datetime.datetime(2024, 11, 15),
    datetime.datetime(2024, 12, 25),
    datetime.datetime(2024, 12, 26),
    datetime.datetime(2024, 12, 27),
    datetime.datetime(2024, 12, 28),
    datetime.datetime(2024, 12, 30),
    datetime.datetime(2024, 12, 31)
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        absences = int(request.form['absences'])
        attendance_percentage = calculate_attendance(start_date, end_date, absences, holidays)
        return render_template('index.html', attendance_percentage=f"{attendance_percentage:.2f}%")
    return render_template('index.html', attendance_percentage=None)

def calculate_attendance(start_date, end_date, absences, holidays):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    
    total_days = (end_date - start_date).days + 1
    total_working_days = 0
    
    for single_date in (start_date + datetime.timedelta(n) for n in range(total_days)):
        if single_date.weekday() < 5 and single_date not in holidays:
            total_working_days += 1
    
    attendance_days = total_working_days - absences
    attendance_percentage = (attendance_days / total_working_days) * 100
    
    return attendance_percentage

if __name__ == '__main__':
    app.run(debug=True)
