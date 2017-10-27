var gulp = require("gulp");
var stylus = require("gulp-stylus");
var plumber = require("gulp-plumber");
var browserSync = require("browser-sync");
var notify = require("gulp-notify");
var pug = require("gulp-pug");

gulp.task('default', ['stylus', 'browser-sync', 'pug', 'watch']);

//sassとpugの監視をして変換処理させる
gulp.task('watch', () => {
    gulp.watch(['./style/**'], () => {
        gulp.start(['stylus']);
    });
    gulp.watch(['./pug/**'], () => {
        gulp.start(['pug']);
    });
});

//ブラウザ表示
gulp.task('browser-sync', () => {
    browserSync({
        server: {
            baseDir: "./"   //サーバとなるrootディレクトリ
        }
    });
    //ファイルの監視
    //以下のファイルが変わったらリロードする
    gulp.watch("./js/**/*.js",     ['reload']);
    gulp.watch("../*.html",         ['reload']);
});

//stylusをcssに変換
gulp.task("stylus", () => {
    gulp.src("./style/**/*styl")
        .pipe(plumber({
            errorHandler: notify.onError("Error: <%= error.message %>")
        }))
        .pipe(stylus())
        .pipe(gulp.dest("./css"))
        //reloadせずにinjectする
        .pipe(browserSync.stream())
});

//pugをhtmlに変換
gulp.task("pug", () => {
    var option = {
        pretty: true
    }
    gulp.src("./markup/**/*.pug")
        .pipe(plumber({
            errorHandler: notify.onError("Error: <%= error.message %>")
        }))
        .pipe(pug(option))
        .pipe(gulp.dest("../"))
});

//ブラウザリロード処理
gulp.task('reload', () => {
    browserSync.reload();
});
