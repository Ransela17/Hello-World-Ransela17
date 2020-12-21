

fetch('https://reqres.in/api/users?page=2').then(response => response.json())
    .then(responseJSON => createUsersList(responseJSON.data)).catch(err => console.log(err));

    function createUsersList(users){
        console.log(users)
        const curr_main = document.querySelector("main")

        for (let user of users) {
            const section = document.createElement("section");
            section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
                <span class="full_name">${user.first_name} ${user.last_name}</span>
                <br>
                <br>
                <a href="mailto:${user.email}">Send Email</a>
                <hr>
            </div>
            `; 
            curr_main.appendChild(section);
        }
    }
