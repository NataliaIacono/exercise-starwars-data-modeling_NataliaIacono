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
    comprobacion_inicio=Column(Integer, ForeignKey("usuarios_contrasenas.id_usuario")) #esto lo necesito de usuarios_contrasenas, CLAVE FORANEA
    

class Usuarios_Contrasenas(Base):
    __tablename__ = 'usuarios_contrasenas'
    id_usuario= Column(Integer, primary_key=True)
    nombre_usuario=Column(String)
    contrasena=Column(String)
    relacion_usuario=relationship("Usuario", backref="usuarios_contrasenas")
    #Hago la relacion a Usuario para poder darle nombre_usuario y contrasena
    relacion_favoritos=relationship("Favoritos", backref="usuarios_contrasenas")

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
    id_usuario= Column(Integer, ForeignKey("usuarios_contrasenas.id_usuario"), primary_key=True) #necesito id_usuario de usuarios_contrasenas
    id_planeta= Column(Integer, ForeignKey("planetas.id_planeta"))
    id_personaje= Column(Integer, ForeignKey("personajes.id_personaje"))
    id_vehiculo= Column(Integer, ForeignKey("vehiculos.id_vehiculo"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
