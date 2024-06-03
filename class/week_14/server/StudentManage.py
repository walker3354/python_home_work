from StudentInfoTable import StudentInfoTable
from SubjectInfoTable import SubjectInfoTable


class StudentManage:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable(parameters)

    def show(self):
        student_name_list = self.student_table.get_all_student()
        return_message = {"status": "OK", "parameters": {}}
        for student_name in student_name_list:
            student_subjects = self.subject_table.get_student_all_subject(
                self.student_table.select_a_student(student_name)
            )
            if len(student_subjects) != 0:
                return_message["parameters"].update(
                    {student_name: {"name": student_name, "scores": student_subjects}}
                )
        return return_message

    def add(self):
        stu_id = self.student_table.insert_a_student(self.parameters["name"])
        self.subject_table.insert_student_all_subject(stu_id)
        return {"status": "OK"}

    def query(self):
        stu_id = self.student_table.select_a_student(self.parameters["name"])
        if not stu_id:
            return {"status": "Fail", "reason": "The name is not found."}
        else:
            student_subjects = self.subject_table.get_student_all_subject(stu_id)
            return {"status": "OK", "scores": student_subjects}

    def modify(self):
        stu_id = self.student_table.select_a_student(self.parameters["name"])
        self.subject_table.del_student_all_subject(stu_id)
        self.subject_table.insert_student_all_subject(stu_id, "_dict")
        return {"status": "OK"}

    def delete(self):
        stu_id = self.student_table.select_a_student(self.parameters["name"])
        self.student_table.delete_a_student(stu_id)
        self.subject_table.del_student_all_subject(stu_id)
        return {"status": "OK"}
