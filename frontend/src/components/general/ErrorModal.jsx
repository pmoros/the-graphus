import { Modal, Button, Card, Row, Col } from "react-bootstrap"

function ErrorModal (props) {

  return(
    <Modal
      {...props}
      size="md"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Maintenance
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Card>
          <Row>
            <Col>
              <Card.Img width="100" height="100"  src="https://img.icons8.com/external-icongeek26-linear-colour-icongeek26/460/000000/external-maintenance-car-service-icongeek26-linear-colour-icongeek26.png" />
            </Col>
            <Col xs={8}>
              <Card.Body>
                <Card.Text>Unfortunately the function is down for a bit of maintenance right now. But soon we'll be up.</Card.Text>
              </Card.Body>
            </Col>
          </Row>
        </Card>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  )
}

export default ErrorModal