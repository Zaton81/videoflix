import reflex as rx
from videoflix.queries.seriesQueries import Series_queries 
from videoflix.queries.filmQueries import Film_queries

#dado que el uso de la clase conjunta para la carga de imágenes ha dado problemas, se ha activado esta opción en las
#distintas clases se subida de series y películas, quedando temporalmente esta clase en desuso

class Upload(rx.State):
    '''clase upload
    verifica el archivo cargado y guarda la imagen'''
    img: list[str]

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        
        for file in files:
            upload_data = await file.read()
            
            outfile = rx.get_upload_dir() / file.filename
            

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)
            print(file.filename)      
              
            
        return  Series_queries.set_portada(file.filename)

    @rx.event 
    async def upload_series(self, files: list[rx.UploadFile]):
        await self.handle_upload(files)

        return Series_queries.add_serie()

 