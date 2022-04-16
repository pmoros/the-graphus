import { useState } from "react";
import { Nav, Navbar, Button, NavDropdown } from "react-bootstrap";
import { Link } from "react-router-dom"

import ErrorModal from "./ErrorModal";
import LoginModal from "../LoginModal";

function Header () {
  const [user, setUser] = useState('User Name')
  const [isLogged, setIsLogged] = useState(true)
  const [errorModalShow, setErrorModalShow] = useState(false)
  const [loginModalShow, setLoginModalShow] = useState(false)

  const handleLogin = () => { setIsLogged(!isLogged) }

  return (
    <>
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
        <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
        {
          isLogged ?
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav variant="dark">
              <Nav.Link variant="dark" onClick={() => setLoginModalShow(true)}>Login</Nav.Link>
            </Nav>
          </Navbar.Collapse>        
          :
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="ml-auto">
              <Nav.Link><Link to="/Curriculum">Curriculum</Link></Nav.Link>
              <Nav.Link><Link to="/Progress">Progress</Link></Nav.Link>
              <Nav.Link><Link to="/Schedule">Schedule</Link></Nav.Link>
            </Nav>
            <Nav className="mr-auto">
              <NavDropdown title={`Signed as: ${user}`} id="basic-nav-dropdown">
                <NavDropdown.Item onClick={() => setErrorModalShow(true)}>User Information</NavDropdown.Item>
                <NavDropdown.Item onClick={() => setErrorModalShow(true)}>Configuration</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item onClick={handleLogin}>Logout</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        }
      </Navbar>
      <LoginModal show={loginModalShow} onHide={() => setLoginModalShow(false) } handleLogin={handleLogin}/>
      <ErrorModal show={errorModalShow} onHide={() => setErrorModalShow(false)}/>
    </>
  )
}

export default Header