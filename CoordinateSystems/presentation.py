from manim import *

class Presentation(ThreeDScene):
    def construct(self):

        self.next_section("Coordinate def")
        #generating text for the coordinate and system of coordinates concepts explanation
        text_coord = MarkupText(f"¿Qué es una <span fgcolor='{RED}'>coordenada</span>?")
        coord_def = MarkupText(f'''Una <span fgcolor='{RED}'>coordenada</span> es un conjunto
        de elementos que representan
        una posición en un espacio determinado''')
        self.play(Create(text_coord))
        self.wait(3)
        self.play(FadeOut(text_coord))
        self.play(Create(coord_def))
        self.wait(3)
        self.play(FadeOut(coord_def))
        del text_coord
        self.next_section("Utility of coordinate systems")
        text_coord_sys = MarkupText(f"¿Qué es un <span fgcolor='{BLUE}'>sistema de coordenadas</span>?")
        self.play(FadeIn(text_coord_sys))
        self.wait(3)
        self.play(FadeOut(text_coord_sys))
        del text_coord_sys
        utility_text_aux = [f'''
        Supongamos que se se quiere definir la ubicación o posición de objetos
        ya sea en un plano, un espacio o superficie por medio de un
        <span fgcolor="{BLUE}">"sistema de coordenadas".</span>''',
        f'''
        Con la intención de hacer varios tipos de mediciones como
        el cálculo de <span fgcolor="{RED}">áreas </span> o <span fgcolor="{RED}">volúmenes</span>, también,
        <span fgcolor="{RED}">ángulos</span>, el <span fgcolor="{RED}">área de superficies</span>, entre otros.
        ''',
        f'''
        Entonces un <span fgcolor="{BLUE}">sistema de coordenadas</span> es el conjunto de todas
        las <span fgcolor='{RED}'>coordenadas</span> posibles en el espacio definido.
        ''',
        f'''
        Entonces, un <span fgcolor="{BLUE}">sistema de coordenadas</span> es el grupo de
        <span fgcolor="{RED}">convenciones</span> que un observador emplea para la <span fgcolor="{RED}">medición</span> o
        <span fgcolor="{RED}">cuantificación</span> de algo en particular, lo que esto quiere decir es que
        dichas magnitudes están vinculadas al <span fgcolor="{BLUE}">sistema de coordenadas</span>,
        asimismo, se encuentran <span fgcolor="{RED}">representadas</span> en este.
        A cada una de estas se le asigna una <span fgcolor="{RED}">coordenada</span> de referencia.
        ''',
        f'''
        Adicionalmente, el <span fgcolor="{BLUE}">sistema de coordenadas</span> tiene
        un <span fgcolor="{RED}">punto de referencia</span> que se puede definir
        según el <span fgcolor="{RED}">interés</span> del que lo usa.
        ''']
        #controling time of display
        for _ in utility_text_aux:
            utility_text = MarkupText(_, font_size=30)
            self.play(Create(utility_text))
            self.wait(5)
            self.play(FadeOut(utility_text))
            del utility_text
        del utility_text_aux
        self.wait(3)
        self.next_section("Algunos sistemas coordenados")
        some_coords_title = MarkupText(f'Algunos <span fgcolor="{BLUE}"> sistemas coordenados</span>') #title
        self.play(FadeIn(some_coords_title))
        self.wait(3)
        self.play(FadeOut(some_coords_title))
        self.wait(1)
        dot = Dot(ORIGIN) #creting a dot that references the origin
        plane = NumberPlane() #plane of numbers
        self.play(Create(plane, run_time=3)) #creating the cartesian plane
        self.add(dot) #placing the origin on the plane
        origin_text = Text('Origen o punto de referencia').next_to(dot, DOWN) #labeling origin
        self.play(Create(origin_text)) #putting the animation for origin label
        self.wait(1)
        self.remove(origin_text) #removing origin label
        del origin_text
        dot.color = YELLOW
        self.wait(1)

        #creating lines to show displacement
        line_hor = Line(ORIGIN, ORIGIN)
        line_vert = Line(2*RIGHT, 2*RIGHT)
        self.add(line_hor, line_vert)
        line_hor.color, line_vert.color = YELLOW, YELLOW
        #generating dot displacement
        for i in range(1, 5):
            if i <= 2: #horizontal displacement
                self.play(
                    dot.animate.shift(RIGHT),
                    line_hor.animate.put_start_and_end_on(ORIGIN, RIGHT*i))
                self.wait(0.5)
                if i == 2: #drawing the brace
                    brace_aux_one = Brace(line_hor)
                    text_aux_one = Text("Movimiento en la primera dimensión", font_size=25).next_to(brace_aux_one, DOWN)
                    self.play(Create(brace_aux_one), Create(text_aux_one))
                    self.wait(1.5)
                    self.remove(brace_aux_one, text_aux_one)
            else: #vertical displacement
                self.play(
                    dot.animate.shift(UP),
                    line_vert.animate.put_start_and_end_on(2*RIGHT, 2*RIGHT + (i-2)*UP))
                self.wait(0.5)
                if i == 4: #drawig the brace
                    brace_aux_one = Brace(line_vert, direction=RIGHT)
                    text_aux_one = Text("Movimiento en la segunda dimensión", font_size=25).next_to(brace_aux_one, UP)
                    self.play(Create(brace_aux_one), Create(text_aux_one))
                    self.wait(1.5)
                    self.remove(brace_aux_one, text_aux_one)
        
        self.remove(line_hor, line_vert)
        del line_hor, line_vert, brace_aux_one, text_aux_one
        arrow_repr_one = Arrow(ORIGIN, [2, 2, 0], buff=0) #creating an arrow that points to (2, 2)
        self.add(arrow_repr_one)
        object_repr_text_one = Text("Representación del objeto en el sistema de coordenadas", font_size=25)
        object_repr_text_one.next_to(dot, UP)
        self.add(object_repr_text_one)
        self.wait(3)
        self.remove(arrow_repr_one, object_repr_text_one, dot)
        self.play(FadeOut(plane))
        del dot, arrow_repr_one, object_repr_text_one, plane
        #showing mapping from cartesian to polar
        def polar2c(p):
            return np.array([
                p[0]*np.cos(p[1]),
                p[0]*np.sin(p[1]),
                0
                ])
        #animating the mapping 
        change_system = Text("¿Y si cambiamos el punto de vista?", font_size=25)
        cartesian_some = NumberPlane(x_range=(-PI, PI, PI/4), y_range=(-PI, PI, PI/4))
        circle_cart = Circle(radius=PI/2) #circle in cartesian coordinates
        self.play(Create(change_system))
        self.wait(2)
        self.play(change_system.animate.shift(3.5*UP))
        self.add(cartesian_some)
        self.play(Create(circle_cart))
        cartesian_some.generate_target()
        cartesian_some.target.prepare_for_nonlinear_transform()
        cartesian_some.target.apply_function(lambda p: polar2c(p))
        self.play(FadeOut(circle_cart))
        self.play(
            MoveToTarget(cartesian_some, run_time=5)
        )
        #generating the transformed circle
        transformed_circle = FunctionGraph(lambda x: PI/2, x_range=[-PI, PI], color=RED)
        cartesian_some.add(transformed_circle)
        self.add(cartesian_some)
        self.wait(3)
        self.play(FadeOut(cartesian_some))
        self.remove(change_system)
        del cartesian_some, change_system, transformed_circle, circle_cart
        self.wait(3)
        #introducing 3D coordinates
        change_dim = Text("¿Y si cambiamos el punto de vista y la dimensión?", font_size=25)
        self.play(Create(change_dim))
        self.wait(2)
        self.play(change_dim.animate.shift(3.5*UP))
        #starting 3d objects
        axes = ThreeDAxes( #third dimensional axes
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            z_range=(-4, 4, 1),
            x_length=8,
            y_length=8,
            z_length=8
        )

        #shpere parametrizatio
        def createSphere(u, v):
            x = 3*np.cos(u)*np.sin(v)
            y = 3*np.sin(u)*np.sin(v)
            z = 3*np.cos(v)

            return np.array([x, y, z])

        #radial section on xy plane of the first octant
        def down(u, r):
            x = r*np.cos(u)
            y = r*np.sin(u)
            z = 0
            return np.array([x, y, z])
        
        #radial section on yz plane of the first octant
        def sideo(u, r):
            x = 0
            y = r*np.sin(u)
            z = r*np.cos(u)
            return np.array([x, y, z])

        #radial section on xz plane of the first octant
        def sides(u, r):
            x = r*np.sin(u)
            y = 0
            z = r*np.cos(u)
            return np.array([x, y, z])

        #generating all the components of the displayed sphere-like figures
        solid_sphere = Surface(
            lambda u, v: createSphere(u, v),
            u_range=[0, 2*PI], v_range=[0, PI],
            fill_opacity=1
        )
        sphereup = Surface(
            lambda u, v: createSphere(u, v),
            u_range= [PI/2, 2*PI], v_range=[0, PI/2],
            fill_opacity=0.1, resolution=40
            )
        spheredown = Surface(
            lambda u, v: createSphere(u, v),
            u_range= [0, 2*PI], v_range=[PI/2, PI],
            fill_opacity=0.1, resolution=40 
            )
        s_down = Surface(
            lambda u, v: down(u, v),
            u_range= [0, PI/2], v_range=[0, 3],
            fill_opacity=1, resolution=40 
            )
        s_sideo = Surface(
            lambda u, v: sideo(u, v),
            u_range= [0, PI/2], v_range=[0, 3],
            fill_opacity=1, resolution=40 
            )
        s_sides = Surface(
            lambda u, v: sides(u, v),
            u_range= [0, PI/2], v_range=[0, 3],
            fill_opacity=1, resolution=40 
            )
        
        #changing color attributes of displayed objects
        solid_sphere.color = BLUE
        sphereup.color = BLUE
        spheredown.color = BLUE
        s_down.color = RED
        s_sides.color = RED
        s_sideo.color = RED
       
        #making animation on spherical coordinates
        self.play(FadeOut(change_dim))
        self.play(axes, Create(solid_sphere))
        self.wait(3)
        self.play(FadeOut(solid_sphere))
        self.add(sphereup, spheredown, s_down, s_sideo, s_sides)
        self.set_camera_orientation(theta=PI/3, phi=PI/4)
        self.wait(5)
        self.remove(axes, sphereup, spheredown, s_down, s_sideo, s_sides)

        


        