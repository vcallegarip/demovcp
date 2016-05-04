module.exports = function(grunt) {

  // 1. All configuration goes here
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      build: {
          src: [
            'src/assets/js/dashboard/*.js',
            'src/assets/js/*.js',
            'src/assets/js/authentication/*.js'
          ],
          dest: 'src/assets/app.js'
      }
    },

    cssmin: {
      options: {
        shorthandCompacting: false,
        roundingPrecision: -1
      },
      target: {
        files: {
          'src/assets/app.css': [
            'src/assets/css/dashboard/*.css',
            'src/assets/css/*.css',
            'src/assets/fonts/google-fonts/*.css'
          ]
        }
      }
    },

    watch: {
      options: {
        livereload: true,
      },
      scripts: {
        files: [
          'src/assets/js/dashboard/*.js',
          'src/assets/js/*.js',
          'src/assets/js/authentication/*.js'
        ],
        tasks: ['uglify'],
        options: {
            spawn: false,
        },
      },

      css: {
          files: [
            'src/assets/css/dashboard/*.css',
            'src/assets/css/*.css',
            'src/assets/fonts/google-fonts/*.css'
          ],
          tasks: ['cssmin'],
          options: {
              spawn: false,
          }
      }
    }

  });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['uglify','cssmin','watch']);

};
