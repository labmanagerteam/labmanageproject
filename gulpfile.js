/**
 * Created by Zhao Guoyan on 2015/7/25.
 */
var gulp = require('gulp'),
    watch = require('gulp-watch');
    minifycss = require('gulp-minify-css'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    del = require('del');

gulp.task('default', function () {
    // place code for your default task here
});

gulp.task('minifycss', function() {
    return gulp.src('src/*.css')      //压缩的文件
        .pipe(gulp.dest('minified/css'))   //输出文件夹
        .pipe(minifycss());   //执行压缩
});

gulp.task('minifyjs', function() {
    return gulp.src('src/*.js')
        .pipe(concat('main.js'))    //合并所有js到main.js
        .pipe(gulp.dest('minified/js'))    //输出main.js到文件夹
        .pipe(rename({suffix: '.min'}))   //rename压缩后的文件名
        .pipe(uglify())    //压缩
        .pipe(gulp.dest('minified/js'));  //输出
});

gulp.task('stream', function () {
    return gulp.src('static/css/*.css')
        .pipe(watch('static/css/*.css'))
        .pipe(gulp.dest('build'));
});

gulp.task('callback', function (cb) {
    watch('static/css/*.css', function () {
        gulp.src('static/css/*.css')
            .pipe(watch('static/css/*.css'))
            .on('end', cb);
    });
});

gulp.task('watch', function (cb) {
    watch('static/css/*.css', function () {
        gulp.src('static/css/*.css')
            .pipe(watch('static/css/*.css'))
            .on('end', cb);
    });
});