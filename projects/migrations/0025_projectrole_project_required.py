import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_backfill_projectrole_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrole',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_roles', to='projects.project'),
        ),
    ]
