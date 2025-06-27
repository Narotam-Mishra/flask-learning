import { useState } from 'react'

const ContactForm = ({ existingContact = {}, updateCallback }) => {
  const [firstName, setFirstName] = useState(existingContact.firstName || "")
  const [lastName, setLastName] = useState(existingContact.lastName || "")
  const [email, setEmail] = useState(existingContact.email || "")

  const updating = existingContact && Object.keys(existingContact).length !== 0;

  const onSubmitHandler = async (e) => {
    e.preventDefault()

    const data = {
        firstName,
        lastName,
        email
    }

    const apiUrl = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : `create_contact`)
    const options = {
        method: updating ? "PATCH" : "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }

    try {
      const response = await fetch(apiUrl, options);
      if(response.status !== 201 && response.status !== 200){
          const data = await response.json();
          alert(data.message)
      } else {
          updateCallback()
      }
    } catch (error) {
      alert("Network error: " + error.message);
    }
  }

  return (
    <>
      <form onSubmit={onSubmitHandler}>
        <div>
          <label htmlFor="firstName">First Name:</label>
          <input
            type="text"
            id="firstName"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="lastName">Last Name:</label>
          <input
            type="text"
            id="lastName"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <button type='submit'>{updating ? "Update" : "Create"}</button>
      </form>
    </>
  );
}

export default ContactForm