from django.core.management.base import BaseCommand, CommandError
import psycopg2
from diseases.models import Disease

class Command(BaseCommand):
    help ='Updates local database'

    def handle(self, *args, **kwargs):
        print('Por favor, aguarde...')
        try:
            conn = psycopg2.connect("dbname='d5mma0lt0jpjfj' user='ekvytxmooqboqc' host='ec2-107-21-122-38.compute-1.amazonaws.com' password='638c124d07e29a9bdf595724d3293a39b2b84f9c2b3f8fe6878e7975fca6efeb'")
        except:
            print('Não foi possível conectar com a base de dados')
            return

        cur = conn.cursor()

        cur.execute("""select * from Pheno_Db""")

        rows = cur.fetchall()


        Disease.objects.all().delete()

        
        to_create = []
        for row in rows:
            if row[2] != None:
                to_create += [Disease(id=row[0], name=row[2], gene=row[1])]


        Disease.objects.bulk_create(to_create)
        print('DONE!')
        