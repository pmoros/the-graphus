import { useState } from "react";
import { Nav, Navbar, Button, NavDropdown } from "react-bootstrap";
import { Link } from "react-router-dom"

function Header () {
  const [isLogged, setIsLogged] = useState(true)
  const [user, setUser] = useState('Andres')

  const handleLogin = () => { setIsLogged(!isLogged) }

  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Navbar.Brand className="justify-content-center">
        <img
          src="https://img.icons8.com/office/480/000000/react.png"
          width="30"
          height="30"
          className="d-inline-block align-top"
          alt="React Bootstrap logo"
        />{' '}
        <Link to="/">The Graphus Project</Link>
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      {
        isLogged ?
        <Navbar.Text>
          <Button variant="link" onClick={handleLogin}>Login</Button>
        </Navbar.Text>
        :
        <>
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link><Link to="/Curriculum">Curriculum</Link></Nav.Link>
              <Nav.Link><Link to="/Progress">Progress</Link></Nav.Link>
            </Nav>
          </Navbar.Collapse>
          <NavDropdown title={`Signed as: ${user}`} id="basic-nav-dropdown">
            <NavDropdown.Item >User Information</NavDropdown.Item>
            <NavDropdown.Item >Configuration</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item onClick={handleLogin}>Logout</NavDropdown.Item>
          </NavDropdown>
        </>
      }
      
      
      
    </Navbar>
  )
}

export default Header