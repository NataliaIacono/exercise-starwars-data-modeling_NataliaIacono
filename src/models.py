import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario (Base):
    __tablename__ = 'usuario'
    id_usuario= Column(Integer, primary_key=True) 
    first_name= Column(String, nullable=False)
    last_name=Column(String)
    nombre_usuario=Column(String, nullable=False ) 
    contrasena=Column(String, nullable=False) 
    email=Column(String, nullable=False)
    address=Column(String)

    relacion_favoritos = relationship("Favoritos", backref="usuario")

    
class Planetas(Base):
    __tablename__ = 'planetas'
    id_planeta= Column(Integer, primary_key=True)
    nombre=Column(String)

    relacion_favoritos=relationship("Favoritos", backref="planetas")

class Personajes(Base):
    __tablename__ = 'personajes'
    id_personaje= Column(Integer, primary_key=True)
    nombre=Column(String)

    relacion_favoritos=relationship("Favoritos", backref="personajes")

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id_vehiculo= Column(Integer, primary_key=True)
    nombre=Column(String)

    relacion_favoritos=relationship("Favoritos", backref="vehiculos")

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id_usuario= Column(Integer, ForeignKey("usuario.id_usuario"), primary_key=True) #necesito id_usuario de usuarios
    planeta= Column(String, ForeignKey("planetas.nombre"))
    personaje= Column(String, ForeignKey("personajes.nombre"))
    vehiculo= Column(String, ForeignKey("vehiculos.nombre"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
