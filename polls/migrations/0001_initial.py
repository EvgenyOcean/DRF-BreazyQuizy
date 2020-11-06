# Generated by Django 3.1.3 on 2020-11-06 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('variant', models.CharField(choices=[('SS', 'Single Selection'), ('MS', 'Multiple Selection'), ('T', 'Text Answer')], max_length=2)),
                ('order', models.IntegerField(default=0)),
                ('correct_answer', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('is_active', models.BooleanField()),
                ('slug', models.SlugField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='UserQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_finished', models.DateTimeField(blank=True, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.choiceanswer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
                ('user_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.userquiz')),
                ('users_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.textanswer')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='user',
            field=models.ManyToManyField(related_name='quizes', through='polls.UserQuiz', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.quiz'),
        ),
        migrations.AddField(
            model_name='choiceanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.question'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.CheckConstraint(check=models.Q(variant__in=['SS', 'MS', 'T']), name='polls_question_variant_valid'),
        ),
    ]
