import { Navbar, Container } from 'react-bootstrap'

function Footer () {
  return (
    <Navbar variant="dark" bg="dark" fixed="bottom">
      <Container>
        <Navbar.Text>Footer</Navbar.Text>
      </Container>
    </Navbar>
  )
}

export default Footer