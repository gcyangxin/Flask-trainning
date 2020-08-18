ready=$(document).ready


ready(function(){
    $('#message').keyup(function(){
        var count=$('#message').val().length;
        $('#count').html(count+'/128');
    })
})

ready(function(){
    $('.commentsCount').click(function(){
        var post_id=$(this).parents('.post').attr('id').replace('post_','');
        var old=$(this).parents('.post').children('.newComment');
        var form=old.children('form')
        var textarea=form.children('textarea');
        // console.log(form);
        var action=form.attr('action');
        action=action.replace('newreply','newcomment');
        action=action.replace(/\d+$/i,post_id);


        textarea.attr('placeholder','comment');

        form.attr('action',action);

        old.toggle();
        event.stopPropagation();
    })
})
ready(function(){
    $('.replys,.comments').click(function(){
        var comment_id=$(this).attr('id').replace('comment_','');
        var old=$(this).parents('.sentComment').siblings('.newComment');
        var username=$(this).attr('username');
        var form=old.children('form')
        var textarea=form.children('textarea');
        var action=form.attr('action');
        action=action.replace('newcomment','newreply');

        action=action.replace(/\d+$/i,comment_id);


        textarea.attr('placeholder','reply:'+username);

        form.attr('action',action);

        old.toggle();
        event.stopPropagation();
    })
})
ready(function(){
    $('.threeCircle svg').click(function(event){
        $(this).next().toggle();
        event.stopPropagation();
    })
})

ready( function(){
    $('body').click(function(){
        $('.threeCircle ul').hide()
    })
})
ready(function(){
    $('#btn-detail').click(function(){
        $('#frm-detail').toggle();
    })
})
ready(function(){
    $('#btn-avatar').click(function(){
        $('#frm-avatar').toggle();
    })
})
