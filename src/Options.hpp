#pragma once

#include <string>
#include <vector>


struct Options
{
    std::string hostname;
    int startPort = 13370;
    int port;
    int numRanks, thisRank;
    int numDebugRanks;
    bool debugThisRank = true;
    std::string appName;
    std::vector<char *> execArgs;
    bool help = false;
    std::string helpString;

    Options(int argc, char ** argv);
    
private:
    enum class Option { help, port, ranks, gdbserver, stopParse, invalid, nonOption };

    static const std::string helpString_base;
    std::string gdbserverPath = "gdbserver";
    std::vector<std::string> debuggerArgs;

    void GenerateExecArgs(int argc, char ** argv, int appArgPos);
    void SetDebugRanks(const std::string & argument);
    static Option ParseOption(const std::string & word);
};


struct OptionsException : public std::exception
{
protected:
    std::string message;

public:
    OptionsException(const std::string & message);
    OptionsException(const std::string & message, int argNum);
    virtual const char * what() const noexcept;
};


struct EnvException : public std::exception
{
protected:
    std::string message;

public:
    EnvException(const std::string & message);
    virtual const char * what() const noexcept;
};