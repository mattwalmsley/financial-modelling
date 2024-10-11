#ifndef FEED_GENERATOR_H
#define FEED_GENERATOR_H

#include <string>
#include <zmq.hpp>

class FeedGenerator {
public:
    FeedGenerator(const std::string& address);
    void start();
private:
    zmq::context_t context;
    zmq::socket_t publisher;
    void send_message(const std::string& message);
};

#endif // FEED_GENERATOR_H
