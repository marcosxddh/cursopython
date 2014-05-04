/**
 * Created by marcos on 04/05/14.
 */

FazerLogin();






function FazerLogin(){

    $("#btnEntrar").button.click(
        function(){
            FazerLogin();

        return false;
        }
    );

    var login = $("#txtLogin").val();
    var senha = $("#txtSenha").val();

    alert(login);


}