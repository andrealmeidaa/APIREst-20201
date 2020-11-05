from init import db,ma

class Marca(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(50),unique=True,nullable=False)

class MarcaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Marca

marca_schema=MarcaSchema()
marcas_schema=MarcaSchema(many=True)

tblessencias=db.Table('perfume_essencia',
db.Column('perfume_id',db.Integer,db.ForeignKey('perfume.id')),
db.Column('essencia_id',db.Integer,db.ForeignKey('essencia.id'))
)

class Essencia(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    descricao=db.Column(db.String(100),unique=True,nullable=False)

class EssenciaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Essencia
        include_relationships=True

essencia_schema=EssenciaSchema()
essencias_schema=EssenciaSchema(many=True)

class Perfume(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(100),nullable=False)
    id_marca=db.Column(db.Integer,db.ForeignKey('marca.id'),nullable=False)
    marca=db.relationship('Marca',backref=db.backref('perfumes',lazy='dynamic'))
    essencias=db.relationship('Essencia',secondary=tblessencias,lazy='subquery',
    backref=db.backref('perfumes', lazy=True))

class PerfumeSchema(ma.SQLAlchemyAutoSchema):
    essencias=ma.Nested(EssenciaSchema,many=True)
    marca=ma.Nested(MarcaSchema)
    class Meta:
        model=Perfume
        #include_relationships=True
        #include_fk=True

perfume_schema=PerfumeSchema()
perfumes_schema=PerfumeSchema(many=True)