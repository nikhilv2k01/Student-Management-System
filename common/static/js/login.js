
        function validate() {
            let username = document.getElementById('username')
            let password = document.getElementById('password')
            let status = 1

            if (username.value == '') {
                document.getElementById('user_err').innerHTML = "*Please enter username"
                document.getElementById('user_err').style.color = "red"
                username.style.borderColor = "red";
                status = 0
            }
            else {
                document.getElementById('user_err').innerHTML = ''
                document.getElementById('username').style.borderColor = ""
                status = 1
            }
            if (password.value == '') {
                document.getElementById('pass_err').innerHTML = "*Please enter password"
                document.getElementById('pass_err').style.color = "red"
                password.style.borderColor = "red";
                status = 0
            }
            else {
                document.getElementById('user_err') = innerHTML = ''
                document.getElementById('password').style.borderColor = ""
                
                status = 1
            }
            if (status == 0) {
                return false
            }

        }
   