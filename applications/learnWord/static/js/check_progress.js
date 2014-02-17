          // set the date we're counting down to
          var count_down_timer = 10000;
          var total_word_play_count      = 10;
          var point_info                 = 0;
var target_date = new Date().getTime() + count_down_timer;

// variables for time units
var days, hours, minutes, seconds;

// get tag element
var countdown = document.getElementById("countdown");
var score_board = document.getElementById("score_board");
var score_point_info = document.getElementById("score_point_info");

// update the tag with id "countdown" every 1 second
var refreshIntervalId = setInterval("count_down_logic();", 1000);

   function count_down_logic(){
       // find the amount of "seconds" between now and target
       var current_date = new Date().getTime();
       var seconds_left = (target_date - current_date) / 1000;


       seconds = parseInt(seconds_left % 60);

       // format countdown string + set tag value
       countdown.innerHTML =  seconds + "s";

       if (seconds ==0) {
           reset_timer_and_display_new_example();
       }

   }






    function reset_count_down_timer(){
        target_date = new Date().getTime() + count_down_timer;
    }
    function start_new_timer_count_down() {
        alert("start new timer");
        target_date = new Date().getTime() + count_down_timer;
        refreshIntervalId = setInterval("count_down_logic();", 1000);
    }
    function clear_word_meanning_explain(){
        document.getElementById("word_meanning_explain_1").innerHTML = ""
        document.getElementById("word_meanning_explain_2").innerHTML = ""
    }

    function reset_timer_and_display_new_word() {
              //reset_count_down_timer();
        clearInterval(refreshIntervalId);
        start_new_timer_count_down();
        ajax('next_word', '', ':eval');
        clear_word_meanning_explain();
          }



    //display example
    function display_new_example(){
              clear_word_meanning_explain();
              ajax('check_example', '', ':eval');

    }
    function reset_timer_and_display_new_example() {
              reset_count_down_timer();
              ajax('check_example', '', ':eval');
              clear_word_meanning_explain();
              clearInterval(refreshIntervalId);
          }
    function check_result_of_selection(){
        alert("check result of selection");

        if_true_increase_count_of_correct_answer()
    }

    function if_true_increase_count_of_correct_answer(){
        score_point_info.innerHTML = point_info + 1;
        point_info = point_info + 1;
    }
    function if_wrong_increase_count_of_correct_answer(){
        alert("decrease point");
     }
    function display_example_of_selection(){
        alert("display example of correct answer");
        clear_word_meanning_explain();
        ajax('check_example', ['meanning_option'], ':eval');
        //clear timer...

        alert("end display example");

    }
    // click button
     $('#user_click_next_button').click(function () {
         reset_timer_and_display_new_word();
    });
     $('#word_meanning_explain_1').click(function () {
              alert("click on select1");
               clearInterval(refreshIntervalId);
             $('#store_value_of_selection').val("option1");
              //check_result_of_selection();
                check_result_of_selection();
              display_example_of_selection();
     });
     $('#word_meanning_explain_2').click(function () {
              alert("click on select2");
              clearInterval(refreshIntervalId);
              $('#store_value_of_selection').val("option2");
              check_result_of_selection();
              display_example_of_selection();
          });

     function update_info_score_board(){
         alert("update info score board");
         score_board.innerHTML = total_word_play_count - 1;
         total_word_play_count = total_word_play_count - 1;
     }
    // detect enter key
          $(document).keypress(function(e) {
              if(e.which == 13) {
                  //alert('You pressed enter!');
                  reset_timer_and_display_new_word();
                  update_info_score_board();
              }
              if(e.which == 32) {
                  //alert('You pressed space!');
                  display_new_example();
              }
          });