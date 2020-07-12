//Not working as expected

#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;
class Request
{
    int _arrival_time;
    int _process_time;

public:
    Request(int arrival_time, int process_time) : _arrival_time(arrival_time), _process_time(process_time) {}

    int arrival_time()
    {
        return _arrival_time;
    }
    int process_time()
    {
        return _process_time;
    }
};
class Response
{
    bool _dropped;
    int _start_time;

public:
    Response(bool dropped, int start_time) : _dropped(dropped), _start_time(start_time) {}

    bool dropped()
    {
        return _dropped;
    }
    int start_time()
    {
        return _start_time;
    }
};

class Buffer
{
    int _size;
    list<int> end_time;

public:
    Buffer(int size) : _size(size) {}

    void delete_processed(Request request)
    {
        while (end_time.size())
        {
            if (end_time[0] <= request.arrival_time())
            {
                end_time.pop_front();
            }
            else
            {
                break;
            }
        };
    }

    Response process(Request request)
    {
        delete_processed(request);
        if (end_time.size() == _size)
        {
            return Response(true, -1);
        }
        if (end_time.size() == 0)
        {
            end_time.push_back(request.arrival_time() + request.process_time());
            return Response(false, request.arrival_time());
        }
        Response response = Response(false, end_time[end_time.size() - 1]);
        end_time.push_back(end_time[end_time.size() - 1] + request.process_time());
        return response;
    }
};

vector<Request> read_requests(int count)
{
    vector<Request> requests;
    for (int i = 0; i < count; ++i)
    {
        int at;
        int pt;
        cin >> at >> pt;
        Response response(at, pt);
        requests.push_back(response);
    }
    return requests;
}

vector<Response> process_requests(vector<Request> requests, Buffer buffer)
{
    vector<Response> processed;
    for (auto r : requests)
    {
        processed.push_back(buffer.process(r));
    }
    return processed;
}

void print_responses(vector<Response> responses)
{
    for (auto response : responses)
    {
        if (response.dropped())
        {
            cout << -1 << endl;
        }
        else
        {
            cout << response.start_time() << endl;
        }
    }
}

int main()
{
    int size;
    int count;
    cin >> size >> count;
    vector<Request> requests = read_requests(count);
    Buffer buffer(size);
    vector<Response> responses = process_requests(requests, buffer);
    print_responses(responses);
    return 0;
}