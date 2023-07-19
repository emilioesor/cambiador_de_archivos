import os
import shutil

from_dir=input("Ingresala carpeta de inicio: ")
to_dir=input("Ingresa la carpeta a la que se moverán los archivos: ")

#almacena nombres de todos los archivos de downloads.
list_of_files= os.listdir(from_dir)
#print(list_of_files)
  
#mover todas las imagenes de la carpeta descargas a otra.
for file_name in list_of_files:
   name, extension= os.path.splitext(file_name)
   #print(name)
   #print(extension)

   if extension==" ":
     continue # reevalua la condicion y saltará al sig archivo y buscara´su extención
   
   if extension in['.txt', '.doc', '.docx','.pdf']:
      #concatena el archivo de origen y el nombre (slash: union)
      path1= from_dir + '/' + file_name
      #carpeta de destino
      path2= to_dir + '/' + "documentos_archivos"
      #carpeta de destino + img del archivo y el nombre con extencion
      path3= to_dir  +'/' + "documentos_archivos" + '/' + file_name
      #imprimir cualquier path 
      # print("path1", path1) o print("path3", path3)  

      #verifica si la carpeta existe, si no creará una carpeta nueva.
      if os.path.exists(path2):
         print("Moviendo" + file_name + "...... ")

         shutil.move(path1,path3)
      else:
         os.makedirs(path2)
         print("Moviendo"+ file_name + ".......")
         shutil.move(path1,path3)
    