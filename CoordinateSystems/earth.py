from manimlib import *

class SurfaceExample(Scene):
    CONFIG = {
        "camera_config":{
            "background_color": BLACK,
            "color": BLACK,
            },
            "camera_class": ThreeDCamera
    } #overridng defalut configurations

    #creating scene
    def construct(self):
        aux_background = Square(side_length=2*FRAME_WIDTH) #generating background square
        aux_background.set_fill(BLACK, opacity=1)
        aux_background.fix_in_frame()
        self.add(aux_background)
        surface_text = Text("La tierra como una esfera") #title
        surface_text.fix_in_frame()
        self.play(FadeIn(surface_text))
        self.wait(1)
        self.play(surface_text.animate.to_edge(UP))
        self.wait(3)

        sphere = Sphere(radius=3) #sphere to cover with earth image later

        #earth image
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"

        surface = TexturedSurface(sphere, day_texture) #covering the sphere

        #displacement of the planet on the canvas
        surface.shift(IN) 
        surface.shift(2*UP)
        surface.mesh = SurfaceMesh(surface) #generating the mesh around the planet
        surface.mesh.set_stroke(BLUE, 1, opacity=1)
        
        #set perspective of the camera
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        #including earth and its mesh on the canvas
        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
        )
        
        surface.add(surface.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2) #rotating the planet
        
        #add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        self.wait(2)
        self.remove(surface, surface.mesh, surface_text)
        
        flat_text = Text("La tierra llevada al plano") #title
        flat_text.fix_in_frame()
        self.play(FadeIn(flat_text)) #incluiding tile
        self.wait(2)
        self.play(FadeOut(flat_text))

        earth_img = ImageMobject(day_texture) #image as flat image
        earth_img.fix_in_frame() #fixing the image on canvas
        earth_img.scale(2) #resizing to cover the whole screen
        frame.add_updater(lambda m, dt: m.increment_theta(0 * dt)) #stopping camera rotation
        self.add(earth_img)
        self.wait(2)
        #addin coordinate system
        axes = Axes(
            x_range=(-180, 180, 20),
            
            y_range=(-90, 90, 10),
            
            height=FRAME_HEIGHT-0.5,
            width=FRAME_WIDTH-0.5,
            
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
           
            y_axis_config={
                "include_tip": False,
            },
            x_axis_config = {
                "include_tip": False,
            },
        )
        #customizing labels
        axes.add_coordinate_labels(
            font_size=10,
            num_decimal_places=1,
        )
        axes.fix_in_frame()
        self.add(axes) #displaying the coordynate system
        self.wait(5)