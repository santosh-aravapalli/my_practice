from django.db import models

# Create your models here.


class physician(models.Model):
    emp_id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=50)
    spectilization = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    ssn = models.IntegerField()

    def __str__(self):
        return self.name


class department(models.Model):
        dept_id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=25)
        head = models.ForeignKey(physician,on_delete=models.CASCADE)

        def __str__(self):
            return self.name


class affliated_with(models.Model):
    physician = models.ForeignKey(physician,on_delete=models.CASCADE)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    is_affliated = models.BooleanField()

    def __str__(self):
        if self.is_affliated == True:
            return "physician : {} is affliated with {} ".format(self.physician.name,self.department.name)
        else:
            return "physician : {} is not affliated".format(self.physician.name)


class procedure(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()


class trained_in(models.Model):
    physician = models.ForeignKey(physician,on_delete=models.CASCADE)
    treatment = models.ForeignKey(procedure,on_delete=models.CASCADE)
    certification_date = models.DateTimeField(auto_now_add=True)
    certification_expires = models.DateTimeField()


class patient(models.Model):
    ssn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    inuranse_id = models.CharField(max_length=30,null=True)
    physician = models.ForeignKey(physician,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class nurse(models.Model):
    emp_id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    registered = models.BooleanField()
    ssn = models.IntegerField()

    def __str__(self):
        return self.name


class appointment(models.Model):
    appointment_id = models.CharField(max_length=15,primary_key=True)
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    duty_nurse = models.ForeignKey(nurse,on_delete=models.CASCADE)
    duty_physician = models.ForeignKey(physician,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateField()
    examin_room = models.CharField(max_length=20)


class medication(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    brand = models.CharField(max_length=30)
    description = models.TextField()


class prescribe(models.Model):
    physician = models.ForeignKey(physician,on_delete=models.CASCADE)
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    medication = models.ForeignKey(medication,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    appointment = models.ForeignKey(appointment,on_delete=models.CASCADE)
    dose = models.TextField()


class block(models.Model):
    blockfloor = models.IntegerField()
    blockcode = models.IntegerField()


class room(models.Model):
    types = [
        ("genral","genral ward"),
        ("AC","Air-Conditioned"),
        ("Non-AC","Non-Air Conditioned")
    ]
    room_number = models.IntegerField()
    room_type = models.CharField(choices=types,max_length=25)
    blockfloor = models.ForeignKey(block,on_delete=models.CASCADE,related_name="room_block_floor")
    blockcode = models.ForeignKey(block,on_delete=models.CASCADE,related_name="room_block_code")
    is_available = models.BooleanField()

    def __str__(self):
        return f"{1}:{2}".format(self.room_number,self.is_available)


class on_call(models.Model):
    nurse = models.ForeignKey(nurse,on_delete=models.CASCADE)
    blockfloor = models.ForeignKey(block,on_delete=models.CASCADE,related_name="on_call_block_floor")
    blockcode = models.ForeignKey(block, on_delete=models.CASCADE,related_name="on_call_block_code")
    on_call_start = models.DateTimeField(auto_now_add=True)
    on_call_end = models.DateTimeField()


class stay(models.Model):
    stay_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    room = models.ForeignKey(room,on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()


class undergoes(models.Model):
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    procedure = models.ForeignKey(procedure,on_delete=models.CASCADE)
    stay = models.ForeignKey(stay,on_delete=models.CASCADE)
    date = models.DateField()
    physician = models.ForeignKey(physician,on_delete=models.CASCADE)
    assist_nurse = models.ForeignKey(nurse,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name


