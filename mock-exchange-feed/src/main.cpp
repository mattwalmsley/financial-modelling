#include "feed_generator.h"

int main() {
    FeedGenerator feed("tcp://*:5555");
    feed.start();
    return 0;
}
