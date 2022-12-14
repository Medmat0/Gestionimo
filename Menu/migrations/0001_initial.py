# Generated by Django 4.0.5 on 2022-07-28 13:29

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, choices=[('HOMME', 'Homme'), ('FEMME', 'Femme')], max_length=10)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('nom', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100, null=True)),
                ('telephone', models.CharField(max_length=100, null=True)),
                ('societe', models.CharField(max_length=100, null=True)),
                ('adresse', models.CharField(max_length=100, null=True)),
                ('codePostal', models.CharField(max_length=100, null=True)),
                ('ville', models.CharField(max_length=100, null=True)),
                ('statut', models.CharField(max_length=100, null=True)),
                ('capitalSocial', models.CharField(max_length=100, null=True)),
                ('numRCS', models.CharField(max_length=100, null=True)),
                ('villeRCS', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metier', models.CharField(max_length=50)),
                ('categorie', models.CharField(choices=[('LOCATION', 'location'), ('VENTE', 'vente')], default=None, max_length=10)),
                ('etape', models.CharField(choices=[('EN_COURS', 'en cours'), ('EN_ATTENTE', 'en attente'), ('EXPIRE', 'expir??')], default=None, max_length=10)),
                ('typeMandat', models.CharField(choices=[('EXCLUSIVE', 'exclusive'), ('NON_EXCLUSIVE', 'non exclusive')], default=None, max_length=20)),
                ('adresse', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=20)),
                ('codePostal', models.CharField(max_length=20)),
                ('affichAdresse', models.CharField(choices=[('OUI', 'oui'), ('NO', 'non')], default='OUI', max_length=10)),
                ('prixNetVendeur', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prixAffiche', models.DecimalField(decimal_places=2, max_digits=5)),
                ('honoraire', models.DecimalField(decimal_places=2, max_digits=5)),
                ('montantHonoraire', models.DecimalField(decimal_places=2, max_digits=5)),
                ('surfaceTotale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('typeBien', models.CharField(choices=[('BUREAU', 'Bureau'), ('LOCAL_COMMERCIAL', 'Local Commercial'), ('TERRAIN', 'Terrain'), ('ENTREPOT', 'Entrep??t')], default=None, max_length=50)),
                ('nombrePieces', models.IntegerField(default=0)),
                ('tailleTerrain', models.DecimalField(decimal_places=2, max_digits=5)),
                ('commentaire', models.TextField(blank=True)),
                ('TitreAnnonce', models.CharField(blank=True, max_length=30)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Transfert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=20)),
                ('codePostal', models.CharField(max_length=20)),
                ('photos', models.ImageField(default='/images/madrid.png', upload_to='uploads/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('Menu.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hauteurMaxConstruction', models.FloatField(default=0)),
                ('coefEmpriseSol', models.IntegerField(default=0)),
                ('prixConstruction', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coefEspaceVert', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Surface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('taille', models.FloatField(default=0)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='produit/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_set', to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Mandat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('honoraire', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('date', models.DateField(default=datetime.date.today)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVisite', models.DateTimeField(default=django.utils.timezone.now)),
                ('honoraireHT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('honoraireTTC', models.DecimalField(decimal_places=2, max_digits=5)),
                ('loyerPropose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('charges', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chargesAcquereur', models.BooleanField(default=False)),
                ('chargesVendeur', models.BooleanField(default=False)),
                ('bail', models.CharField(choices=[('DEROGATOIRE', 'd??rogatoire'), ('COMMERCIAL', 'commercial'), ('PROFESSIONNEL', 'professionnel')], default=None, max_length=20)),
                ('dureeBail', models.IntegerField()),
                ('depotGranti', models.DecimalField(decimal_places=2, max_digits=5)),
                ('taxeFrontiere', models.DecimalField(decimal_places=2, max_digits=5)),
                ('financement', models.BooleanField(default=False)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=5)),
                ('taux', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duree', models.IntegerField()),
                ('permisConstruction', models.BooleanField(default=False)),
                ('droitPreemption', models.BooleanField(default=False)),
                ('faculteSubstitution', models.BooleanField(default=False)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.offre')),
            ],
        ),
        migrations.CreateModel(
            name='LocalCommercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineaireVitrine', models.CharField(max_length=50)),
                ('emplacement', models.CharField(max_length=50)),
                ('derniereActivite', models.DateField(null=True)),
                ('parking', models.CharField(choices=[('OUI', 'oui'), ('NO', 'non')], default='NON', max_length=10)),
                ('detailsParking', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='GED',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Entrepot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HauteurSousPlafond', models.DecimalField(decimal_places=2, max_digits=5)),
                ('typeConstruction', models.CharField(max_length=50)),
                ('ChargesCopropriete', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.TextField(default=None)),
                ('ville', models.CharField(default=None, max_length=20)),
                ('codePostal', models.CharField(default=None, max_length=20)),
                ('prixmax', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('prixmin', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('typeproduit', models.CharField(default=None, max_length=20)),
                ('category', models.CharField(default=None, max_length=20)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVisite', models.DateTimeField(default=django.utils.timezone.now)),
                ('honoraireHT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('honoraireTTC', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prixPropose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('indemnite', models.DecimalField(decimal_places=2, default=5, max_digits=5)),
                ('activite', models.CharField(max_length=50)),
                ('delaiValidite', models.DateTimeField(default=django.utils.timezone.now)),
                ('financement', models.BooleanField(default=False)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=5)),
                ('taux', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duree', models.IntegerField()),
                ('permisConstruction', models.BooleanField(default=False)),
                ('droitPreemption', models.BooleanField(default=False)),
                ('faculteSubstitution', models.BooleanField(default=False)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.offre')),
            ],
        ),
    ]
