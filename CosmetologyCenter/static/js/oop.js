function Service(name, price, time) {
    this.name = name;
    this.price = price;
    this.time = time;
  }

  Service.prototype.getName = function () {
    return this.name;
  };

  Service.prototype.getPrice = function () {
    return this.price;
  };

  Service.prototype.getTime = function () {
    return this.time;
  };

  Service.prototype.getServiceInfo = function () {
    return `Name: ${this.name}, Price: ${this.price}, Time: ${this.time}`;
  };

  function Message(name, price, time, type) {
    Service.call(this, name, price, time);
    this.type = type;
  }

  Message.prototype = Object.create(Service.prototype);

  Message.prototype.getType = function () {
    return this.type;
  };

  Message.prototype.getServiceInfo = function () {
    return `Name: ${this.name}, Price: ${this.price}, Time: ${this.time}`;
  };

const service = new Service("Basic", 50, 30);
document.getElementById("serviceName").innerText = service.getName();
document.getElementById("servicePrice").innerText = service.getPrice();
document.getElementById("serviceTime").innerText = service.getTime();
document.getElementById("serviceInfo").innerText = service.getServiceInfo();

const message = new Message("Relaxing", 80, 60, "Swedish");
document.getElementById("messageName").innerText = message.getName();
document.getElementById("messagePrice").innerText = message.getPrice();
document.getElementById("messageTime").innerText = message.getTime();
document.getElementById("messageType").innerText = message.getType();
document.getElementById("messageInfo").innerText = message.getServiceInfo();

class ServiceClass {
    constructor(name, price, time) {
      this.name = name;
      this.price = price;
      this.time = time;
    }
  
    getName() {
      return this.name;
    }
  
    getPrice() {
      return this.price;
    }
  
    getTime() {
      return this.time;
    }
  
    getServiceInfo() {
      return `Name: ${this.name}, Price: ${this.price}, Time: ${this.time}`;
    }
  }
  
  class MessageClass extends ServiceClass {
    constructor(name, price, time, type) {
      super(name, price, time);
      this.type = type;
    }
  
    getType() {
      return this.type;
    }
  
    getServiceInfo() {
      return `Name: ${this.name}, Price: ${this.price}, Time: ${this.time}, Type: ${this.type}`;
    }
  }

  const serviceClass = new ServiceClass("Basic", 50, 30);
  document.getElementById("serviceNameClass").innerText = service.getName();
  document.getElementById("servicePriceClass").innerText = service.getPrice();
  document.getElementById("serviceTimeClass").innerText = service.getTime();
  document.getElementById("serviceInfoClass").innerText = service.getServiceInfo();
  
  const messageClass = new MessageClass("Relaxing", 80, 60, "Swedish");
  document.getElementById("messageNameClass").innerText = message.getName();
  document.getElementById("messagePriceClass").innerText = message.getPrice();
  document.getElementById("messageTimeClass").innerText = message.getTime();
  document.getElementById("messageTypeClass").innerText = message.getType();
  document.getElementById("messageInfoClass").innerText = message.getServiceInfo();

  console.log("sjk");