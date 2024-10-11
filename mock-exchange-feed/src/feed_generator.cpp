#include "feed_generator.h"
#include <iostream>
#include <thread>
#include <chrono>

// TODO Add more complex logic, such as simulating real market data or using serialization libraries like Protocol Buffers.
// TODO Optimise for low-latency by tuning message-sending and network stack
FeedGenerator::FeedGenerator(const std::string& address)
    : context(1), publisher(context, ZMQ_PUB) {
    publisher.bind(address);
}

void FeedGenerator::send_message(const std::string& message) {
    zmq::message_t zmq_message(message.size());
    memcpy(zmq_message.data(), message.data(), message.size());
    publisher.send(zmq_message, zmq::send_flags::none);
}

void FeedGenerator::start() {
    int tick = 0;
    while (true) {
        std::string message = "Tick: " + std::to_string(tick++);
        send_message(message);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));  // TODO 10 messages per second
    }
}
