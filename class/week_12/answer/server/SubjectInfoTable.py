from DBConnection import DBConnection
from StudentInfoTable import StudentInfoTable


class SubjectInfoTable:
    def __init__(self, parameter={}):
        self.student_dict = parameter

    def insert_student_all_subject(self, student_id, modify_instr=""):
        for subject, score in self.student_dict["scores" + modify_instr].items():
            command = "INSERT INTO subject_info (stu_id, subject, score) VALUES ('{}', '{}', {});".format(
                student_id, subject, score
            )
            with DBConnection() as connection:
                cursor = connection.cursor()
                cursor.execute(command)
                connection.commit()

    def get_student_all_subject(self, student_id):
        command = "SELECT * FROM subject_info WHERE stu_id='{}';".format(student_id)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return_message = dict()
        for row in record_from_db:
            return_message.update({row["subject"]: row["score"]})
        return return_message

    def del_student_all_subject(self, student_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(student_id)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
