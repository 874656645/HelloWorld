(function($) {

    //el操纵对象，option属性值
    $.love = function(el, option) {

        var lo = $(el);
        lo.vars = $.extend({}, $.love.default, option); //合并成新对象，则是新的属性列表

        //定义其他属性
        var scene = null;       // 场景
        var renderer = null;
        var camera = null;


        //私有方法,私有方法之间可互相调用　
        var method = {};
        method = {

            initScene: function() {
                // create a scene, that will hold all our elements such as objects, cameras and lights.
                scene = new THREE.Scene();

                // create a camera, which defines where we're looking at.
                camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);

                // create a render and set the size
                renderer = new THREE.WebGLRenderer();
                renderer.setClearColorHex();
                renderer.setClearColor(new THREE.Color(0xEEEEEE));
                renderer.setSize(window.innerWidth, window.innerHeight);

                // show axes in the screen
                var axes = new THREE.AxisHelper(20);
                scene.add(axes);

                // create the ground plane
                var planeGeometry = new THREE.PlaneGeometry(60, 20);
                var planeMaterial = new THREE.MeshBasicMaterial({color: 0xcccccc});
                var plane = new THREE.Mesh(planeGeometry, planeMaterial);

                // rotate and position the plane
                plane.rotation.x = -0.5 * Math.PI;
                plane.position.x = 15;
                plane.position.y = 0;
                plane.position.z = 0;

                // add the plane to the scene
                scene.add(plane);

                // create a cube
                var cubeGeometry = new THREE.BoxGeometry(4, 4, 4);
                var cubeMaterial = new THREE.MeshBasicMaterial({color: 0xff0000, wireframe: true});
                var cube = new THREE.Mesh(cubeGeometry, cubeMaterial);

                // position the cube
                cube.position.x = -4;
                cube.position.y = 3;
                cube.position.z = 0;

                // add the cube to the scene
                scene.add(cube);

                // create a sphere
                var sphereGeometry = new THREE.SphereGeometry(4, 20, 20);
                var sphereMaterial = new THREE.MeshBasicMaterial({color: 0x7777ff, wireframe: true});
                var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);

                // position the sphere
                sphere.position.x = 20;
                sphere.position.y = 4;
                sphere.position.z = 2;

                // add the sphere to the scene
                scene.add(sphere);

                // position and point the camera to the center of the scene
                camera.position.x = -30;
                camera.position.y = 40;
                camera.position.z = 30;
                camera.lookAt(scene.position);

                // add the output of the renderer to the html element
                lo.append(renderer.domElement);

                // render the scene
                renderer.render(scene, camera);
            },

            initStyle: function() {
                lo.css({
                    // "color": "white",
                    // "background-color": "#98bf21",
                    "width": lo.vars.width,
                    "height": lo.vars.height,
                    // "padding": "5px"
                });
            }
        };

        //公有方法（特权方法），供类外调用
        this.init = function() {
            
            method.initStyle();
            method.initScene();
        };　

        this.hide = function() {

            scene.children.forEach(function(e){

                if (e instanceof THREE.Mesh) {

                    e.visible = false;
                }
                
            });

            // render the scene
            renderer.render(scene, camera);
        };

        this.show = function(){

            scene.children.forEach(function(el){

                if (el instanceof THREE.Mesh) {
                    
                    el.visible = true;
                }
            });

            renderer.render(scene, camera);
        };
    }

    //可设置默认属性
    $.love.default = {
        scene: null,
        width: 500,
        height: 400　
    }

})(jQuery);