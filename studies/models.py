from django.db import models

# from django.contrib.auth.models import User
class Study(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름", null=False)
    github_repository = models.URLField(max_length=200, verbose_name="GitHub 저장소", null=True)
    # members = models.ManyToManyField(User, on_delete=models.SET_NULL, related_name='study_member', verbose_name="멤버")
    # leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='study_leader', verbose_name="리더")
    language = models.CharField(max_length=50, null=True, default=None)
    default_problem_number = models.IntegerField(null=True, default=None)
    start_date = models.DateField ( auto_now = False , auto_now_add = False)
    grade = (('D', '대류권'),('S', '성층권'),('J', '중간권'), ('Y', '열권'), ('O', '외기권')) 
    study_grade = models.CharField(max_length=2, choices=grade)
    is_open = models.BooleanField()
    backjoon_id = models.ForeignKey(to="User", on_delete=models.SET_NULL,related_name='study_backjoon_id', verbose_name="백준 아이디")
    

class Week_study(models.Model):
    study = models.ForeignKey("Study", on_delete=models.CASCADE, verbose_name="해당스터디", null= False)
    week = models.IntegerField(null=False, default=None, verbose_name="주차")
    # problems = models.ManyToManyField("Problem", null=False, verbose_name="문제들")
    algorithms = models.CharField(max_length=50, null=False, verbose_name="알고리즘")


class Notification(models.Model):
    # user = models.ForeignKey(User, null=False)
    study = models.ForeignKey("Study", on_delete=models.CASCADE, null=False)
    title = models.TextField()
    content = models.TextField()
    is_read = models.BooleanField()